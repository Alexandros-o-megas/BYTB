import os
import yt_dlp
import tkinter as tk
from tkinter import messagebox, filedialog

# Caminho para o ffmpeg instalado
CAMINHO_FFMPEG = os.getcwd()  # usa a pasta atual como local do ffmpeg

def baixar(link, tipo, status_label):
    if not link.strip():
        messagebox.showwarning("Aviso", "Insira um link válido.")
        return

    pasta = 'downloads/video' if tipo == 'video' else 'downloads/audio'
    os.makedirs(pasta, exist_ok=True)

    if tipo == 'video':
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'merge_output_format': 'mp4',
            'outtmpl': os.path.join(pasta, '%(title)s.%(ext)s'),
            'ffmpeg_location': CAMINHO_FFMPEG,
            'noplaylist': False
        }
    else:
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(pasta, '%(title)s.%(ext)s'),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'ffmpeg_location': CAMINHO_FFMPEG,
            'noplaylist': False
        }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            status_label.config(text="🔄 Baixando...")
            ydl.download([link])
            status_label.config(text="✅ Download concluído!")
    except Exception as e:
        status_label.config(text="❌ Erro no download")
        messagebox.showerror("Erro", str(e))

def criar_interface():
    janela = tk.Tk()
    janela.title("Q-Download_YouTube")
    janela.geometry("500x250")
    janela.resizable(True, True)

    tk.Label(janela, text="Insira o link do vídeo ou playlist:").pack(pady=10)
    link_entry = tk.Entry(janela, width=60)
    link_entry.pack()

    status_label = tk.Label(janela, text="", fg="blue")
    status_label.pack(pady=10)

    frame_botoes = tk.Frame(janela)
    frame_botoes.pack(pady=10)

    tk.Button(frame_botoes, text="⬇️ Baixar Vídeo", width=20,
              command=lambda: baixar(link_entry.get(), "video", status_label)).grid(row=0, column=0, padx=5)

    tk.Button(frame_botoes, text="🎵 Baixar Áudio (MP3)", width=20,
              command=lambda: baixar(link_entry.get(), "audio", status_label)).grid(row=0, column=1, padx=5)

    tk.Button(janela, text="❌ Sair", command=janela.destroy).pack(pady=10)

    janela.mainloop()

if __name__ == "__main__":
    criar_interface()
