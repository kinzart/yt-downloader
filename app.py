from flask import Flask, request, render_template
import yt_dlp
import os
import threading

app = Flask(__name__)

# Lock global pra evitar duas requisições baixando ao mesmo tempo
DOWNLOAD_LOCK = threading.Lock()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
AUDIOS_DIR = os.path.join(BASE_DIR, "audios")
VIDEOS_DIR = os.path.join(BASE_DIR, "videos")

os.makedirs(AUDIOS_DIR, exist_ok=True)
os.makedirs(VIDEOS_DIR, exist_ok=True)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/download", methods=["POST"])
def download():
    url = request.form["url"]
    tipo = request.form["tipo"]

    if "list=" in url:
        return render_template("confirm.html", url=url, tipo=tipo)

    return baixar(url, tipo, playlist=False)

@app.route("/baixar_video", methods=["POST"])
def baixar_video():
    url = request.form["url"]
    tipo = request.form["tipo"]
    return baixar(url, tipo, playlist=False)

@app.route("/baixar_playlist", methods=["POST"])
def baixar_playlist():
    url = request.form["url"]
    tipo = request.form["tipo"]
    return baixar(url, tipo, playlist=True)

def baixar(url, tipo, playlist):
    # 🔒 evita concorrência (principal pro WinError 32)
    with DOWNLOAD_LOCK:
        if tipo == "video":
            ydl_opts = {
                "outtmpl": os.path.join(VIDEOS_DIR, "%(title).200s [%(id)s].%(ext)s"),
                "format": "bestvideo+bestaudio/best",
                "noplaylist": not playlist,

                # ajuda no Windows (nomes e locks)
                "windowsfilenames": True,
                "nopart": False,          # mantém .part enquanto baixa
                "overwrites": True,       # sobrescrever se existir
            }
        else:
            ydl_opts = {
                "format": "bestaudio/best",
                # ✅ evita colisão (inclui o ID)
                "outtmpl": os.path.join(AUDIOS_DIR, "%(title).200s [%(id)s].%(ext)s"),
                "noplaylist": not playlist,

                "windowsfilenames": True,
                "nopart": False,
                "overwrites": True,

                "postprocessors": [{
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }],
            }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

    return render_template("success.html", tipo=tipo, playlist=playlist)

if __name__ == "__main__":
    # Em produção, use debug=False (o debugger do Flask é perigoso exposto)
      app.run(host="127.0.0.1", port=5000, debug=False, threaded=True)

