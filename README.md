# yt-downloader

YT DOWNLOADER VIA PYTHON COM FRONT EM HTML

## 🎧 YouTube Downloader (Flask + yt-dlp)

Aplicação web para download de vídeos e áudios do YouTube, desenvolvida em **Python + Flask**, utilizando **yt-dlp** e **FFmpeg**.

Interface simples, focada em uso local, com suporte a download de vídeo, áudio (MP3) e playlists.

---

## ✨ Funcionalidades

* Download de **vídeo** (MP4)
* Download de **áudio** (MP3)
* Suporte a **playlist ou vídeo único**
* Interface web simples
* Compatível com **Windows**
* Organização automática em pastas (`audios/` e `videos/`)

---

## 🗂 Estrutura do projeto

```txt
yt-downloader/
├─ app.py                 # Aplicação Flask
├─ requirements.txt       # Dependências Python
├─ templates/             # Templates HTML
│  ├─ index.html
│  ├─ confirm.html
│  └─ success.html
├─ audios/                # Áudios baixados (MP3)
├─ videos/                # Vídeos baixados (MP4)
└─ README.md
```

As pastas `audios/` e `videos/` são criadas automaticamente caso não existam.

---

## 📦 Requisitos

### 1️⃣ Python

* **Python 3.10 ou superior**

Verifique:

```bash
python --version
```

---

### 2️⃣ Dependências Python

Instale todas de uma vez:

```bash
pip install -r requirements.txt
```

---

### 3️⃣ FFmpeg (OBRIGATÓRIO)

O FFmpeg é usado para conversão de áudio (MP3).
Sem ele, o download de áudio não funciona.

---

## 🔧 Como instalar o FFmpeg

### 🪟 Windows

1. Acesse: [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html)
2. Clique em **Windows**
3. Baixe uma versão **static build**
4. Extraia o arquivo `.zip`
5. Mova a pasta para:

   ```
   C:\ffmpeg
   ```
6. Adicione o caminho abaixo ao **PATH do sistema**:

   ```
   C:\ffmpeg\bin
   ```
7. Teste no terminal:

   ```bash
   ffmpeg -version
   ```

Se aparecer a versão, está funcionando corretamente.

---

## ▶️ Como rodar o projeto

### Modo simples

```bash
python app.py
```

Acesse no navegador:

```
http://127.0.0.1:5000
```

---

## 🎯 Como usar

1. Cole a **URL do vídeo ou playlist do YouTube**
2. Escolha o tipo:

   * 🎬 Vídeo
   * 🎧 Áudio (MP3)
3. Confirme o download
4. O arquivo será salvo automaticamente em:

   * `videos/` para vídeo
   * `audios/` para áudio

---

## ⚠️ Observações importantes

* O download depende da disponibilidade do conteúdo no YouTube
* Alguns vídeos podem exigir autenticação ou cookies
* Evite abrir o mesmo download múltiplas vezes ao mesmo tempo
* Use apenas conteúdos que você tem direito de baixar

---

## 🧠 Tecnologias utilizadas

* Python
* Flask
* yt-dlp
* FFmpeg
* HTML / CSS
