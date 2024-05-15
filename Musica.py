from pytube import YouTube
from moviepy.editor import *

def download_video(url):
    yt = YouTube(url)
    # Selecciona el stream con la mejor calidad de audio
    video = yt.streams.filter(only_audio=True).first()
    # Descarga el video
    out_file = video.download(output_path=".")

    # Carga el archivo descargado con MoviePy
    clip = AudioFileClip(out_file)
    # Define el nombre del archivo mp3
    mp3_file = out_file.split('.')[0] + '.mp3'
    # Convierte a mp3
    clip.write_audiofile(mp3_file, codec='libmp3lame')

    return mp3_file

if __name__ == "__main__":
    # URL del video de YouTube que deseas descargar
    url = 'https://www.youtube.com/watch?v=LgH23MlkN1w'
    mp3_filename = download_video(url)
    print(f"Descargado y convertido a MP3 en el archivo: {mp3_filename}")
