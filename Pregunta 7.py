import requests
import sqlite3

def obtener_tipo_cambio_anual():
    url = "https://apis.net.pe/api-tipo-cambio/tipo-cambio-anual"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print("Error al obtener los datos del API de SUNAT")
            return None
    except requests.RequestException as e:
        print("Error de conexión:", e)
        return None

def crear_tabla_sunat_info(conn):
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS sunat_info (
                        fecha TEXT PRIMARY KEY,
                        precio_compra DECIMAL,
                        precio_venta DECIMAL
                      )''')
    conn.commit()

def insertar_datos_sunat_info(conn, data):
    cursor = conn.cursor()
    for registro in data:
        fecha = registro['fecha']
        precio_compra = registro['precio_compra']
        precio_venta = registro['precio_venta']
        cursor.execute('''INSERT INTO sunat_info (fecha, precio_compra, precio_venta)
                          VALUES (?, ?, ?)''', (fecha, precio_compra, precio_venta))
    conn.commit()

def mostrar_contenido_tabla(conn):
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM sunat_info''')
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def main():
    
    data = obtener_tipo_cambio_anual()
    if data is None:
        return

    
    conn = sqlite3.connect('base.db')

    
    crear_tabla_sunat_info(conn)

    
    insertar_datos_sunat_info(conn, data)

    
    print("Contenido de la tabla 'sunat_info':")
    mostrar_contenido_tabla(conn)

    
    conn.close()

if __name__ == "__main__":
    main()
