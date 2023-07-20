import requests
from bs4 import BeautifulSoup

def obtener_contenido_web(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.content
        else:
            print("No se pudo acceder al sitio web. Código de estado:", response.status_code)
            return None
    except requests.exceptions.RequestException as e:
        print("Error al obtener contenido web:", e)
        return None

def extraer_informacion(html):
    # Aquí utilizaremos BeautifulSoup para extraer la información relevante
    # Puedes personalizar esto según la estructura del sitio web que desees analizar
    soup = BeautifulSoup(html, 'html.parser')
    informacion = soup.find('div', class_='contenido').get_text()  # Ejemplo: supongamos que queremos obtener el contenido dentro de un div con clase "contenido"
    return informacion

def guardar_en_bloque_de_notas(contenido, archivo):
    with open(archivo, 'w') as file:
        file.write(contenido)
    print("La información ha sido guardada en el archivo:", archivo)

if __name__ == "__main__":
    url = "https://madrid8342.discord.media/"  # Reemplaza esto con la URL del sitio web que desees obtener
    archivo_salida = "informacion.txt"  # Nombre del archivo donde se guardará la información

    contenido_web = obtener_contenido_web(url)
    if contenido_web:
        informacion_extraida = extraer_informacion(contenido_web)
        guardar_en_bloque_de_notas(informacion_extraida, archivo_salida)
