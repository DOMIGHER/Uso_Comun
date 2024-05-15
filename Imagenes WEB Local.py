from PIL import Image

def convert_image(input_filepath, output_filepath):
    try:
        # Abrir la imagen .webp
        with Image.open(input_filepath) as img:
            # Convertir la imagen a formato RGB y guardarla como JPEG
            if img.format != 'JPEG':
                rgb_image = img.convert('RGB')
                rgb_image.save(output_filepath, 'JPEG')
                print(f"Imagen guardada como {output_filepath} en formato JPEG.")
            else:
                img.save(output_filepath)
                print(f"Imagen ya era JPEG y se ha guardado como {output_filepath}.")
    except IOError as e:
        print(f"Error al procesar la imagen: {e}")

# Ruta del archivo de entrada (imagen .webp local)
input_filepath = "C:/Users/LEGA/Downloads/GUARDAR_TERA/31955128d39b8803bfc8085a69d97130.webp"
# Ruta del archivo de salida (convertido a .jpg)
output_filepath = "C:/Users/LEGA/Downloads/GUARDAR_TERA/imagen_convertida.jpg"

convert_image(input_filepath, output_filepath)
