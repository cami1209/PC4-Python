import requests

def obtener_precio_bitcoin():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        data = response.json()
        precio_usd = data["bpi"]["USD"]["rate_float"]
        return precio_usd
    except requests.RequestException as e:
        print("Error al obtener el precio de Bitcoin:", e)
        return None

def main():
    n_bitcoins = float(input("Ingrese la cantidad de bitcoins que posee: "))
    
    precio_bitcoin = obtener_precio_bitcoin()
    if precio_bitcoin is not None:
        costo_usd = n_bitcoins * precio_bitcoin
        print(f"El costo actual de {n_bitcoins} bitcoins es: ${costo_usd:,.4f}")

if __name__ == "__main__":
    main()
