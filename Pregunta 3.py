import requests
import zipfile
from io import BytesIO

url = "https://images.unsplash.com/photo-1546527868-ccb7ee7dfa6a?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"

response = requests.get(url)

if response.status_code == 200:
   
    zip_buffer = BytesIO()
    with zipfile.ZipFile(zip_buffer, "w") as zip_file:
        zip_file.writestr("imagen.jpg", response.content)

    with open("imagen.zip", "wb") as zip_output:
        zip_output.write(zip_buffer.getvalue())

    print("Imagen descargada y almacenada como archivo ZIP.")
else:
    print("Error al descargar la imagen.")

