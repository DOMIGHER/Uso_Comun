import requests
from PIL import Image
from io import BytesIO

def download_and_convert_image(url, output_filename):
    # Intenta descargar la imagen
    try:
        response = requests.get(url)
        response.raise_for_status()  # Lanza un error en caso de fallo en la descarga
    except requests.RequestException as e:
        print(f"Error al descargar la imagen: {e}")
        return

    # Intenta abrir la imagen y convertirla a JPG
    try:
        image = Image.open(BytesIO(response.content))
        # Convertir la imagen a JPG si no es JPG
        if image.format != 'JPEG':
            rgb_image = image.convert('RGB')  # Convertir a RGB si es necesario
            rgb_image.save(output_filename, "JPEG")
            print(f"Imagen guardada como {output_filename}")
        else:
            image.save(output_filename)
            print(f"Imagen ya era JPG y se ha guardado como {output_filename}")
    except IOError as e:
        print(f"Error al procesar la imagen: {e}")

# URL de la imagen .webp
url = "https://static.wikia.nocookie.net/creepypasta/images/7/7a/Libro_rojo654.jpg/revision/latest?cb=20150906131623&path-prefix=es"
# Nombre del archivo de salida
output_filename = "salida.jpg"

download_and_convert_image(url, output_filename)
