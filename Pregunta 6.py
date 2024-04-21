def contar_lineas_codigo(ruta):
    try:
        # Verificar si la ruta termina en .py
        if not ruta.endswith(".py"):
            print("El archivo no tiene extensión .py")
            return

        # Abrir el archivo y contar las líneas de código excluyendo comentarios y líneas en blanco
        with open(ruta, "r") as file:
            lineas = file.readlines()
            contador = 0
            comentario = False
            for linea in lineas:
                # Eliminar espacios en blanco al inicio y al final de la línea
                linea = linea.strip()
                # Verificar si la línea es un comentario o está en blanco
                if not linea or linea.startswith("#"):
                    continue
                contador += 1
        print(f"Archivo: {ruta}, número de líneas de código: {contador}")
    except FileNotFoundError:
        print("El archivo no existe o la ruta es inválida.")

def main():
    ruta_archivo = input("Ingrese la ruta del archivo .py: ")
    contar_lineas_codigo(ruta_archivo)

if __name__ == "__main__":
    main()
