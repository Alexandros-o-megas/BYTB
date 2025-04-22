import yt_dlp
import os

def baixar(link, path='downloads'):
    # Caminho direto para o ffmpeg (altere se precisar)
    caminho_ffmpeg = r'C:\Users\user\ffpmg\ffmpeg-7.0.2-full_build\bin'

    # Cria a pasta de destino se não existir
    if not os.path.exists(path):
        os.makedirs(path)

    # Opções de download
    ydl_opts = {
        'outtmpl': os.path.join(path, '%(title)s.%(ext)s'),  # Nome do arquivo
        'format': 'bestvideo+bestaudio/best',                # Melhor qualidade
        'merge_output_format': 'mp4',                        # Formato final
        'ffmpeg_location': caminho_ffmpeg,                   # Caminho do ffmpeg
        'noplaylist': False                                  # Permite playlist
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Iniciando download de: {link}\n")
            ydl.download([link])
            print("\n✅ Download concluído com sucesso!")
    except Exception as e:
        print(f"\n❌ Erro ao baixar: {e}")

def main():
    link = input("Insira o link do vídeo ou da playlist do YouTube: ").strip()
    if not link:
        print("❗ Nenhum link foi inserido.")
        return
    baixar(link)

if __name__ == "__main__":
    main()

""""
import yt_dlp
import os

def baixar(link, path='downloads'):
    # Cria pasta se não existir
    if not os.path.exists(path):
        os.makedirs(path)

    # Opções de download
    ydl_opts = {
        'outtmpl': os.path.join(path, '%(title)s.%(ext)s'),
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4',
        'noplaylist': False  # Se for vídeo único, só baixa ele
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Iniciando download de: {link}\n")
            ydl.download([link])
            print("\n✅ Download concluído com sucesso!")
    except Exception as e:
        print(f"❌ Erro ao baixar: {e}")

def main():
    link = input("Insira o link do vídeo ou da playlist do YouTube: ").strip()
    baixar(link)

if __name__ == "__main__":
    main()
    """
