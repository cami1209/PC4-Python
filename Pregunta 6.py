import requests
import json

def obtener_precio_bitcoin():
    try:
        # Consultar la API del índice de precios de Bitcoin de CoinDesk
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        data = response.json()
        
        # Obtener el precio actual de Bitcoin
        precio_usd = data["bpi"]["USD"]["rate_float"]
        return precio_usd
    except requests.RequestException as e:
        print("Error al obtener el precio de Bitcoin:", e)
        return None

def guardar_precio_bitcoin(precio):
    try:
        # Crear un archivo de texto para almacenar el precio de Bitcoin
        with open("precio_bitcoin.txt", "w") as file:
            file.write(f"Precio actual de Bitcoin en USD: {precio:.2f} USD")
        print("Precio de Bitcoin guardado correctamente en precio_bitcoin.txt")
    except IOError as e:
        print("Error al guardar el precio de Bitcoin:", e)

def main():
    # Obtener el precio actual de Bitcoin
    precio_bitcoin = obtener_precio_bitcoin()
    
    if precio_bitcoin is not None:
        # Guardar el precio de Bitcoin en un archivo de texto
        guardar_precio_bitcoin(precio_bitcoin)

if __name__ == "__main__":
    main()
