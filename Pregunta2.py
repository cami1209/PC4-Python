import random
from pyfiglet import Figlet

def main():
    # Crear una instancia de Figlet
    figlet = Figlet()

    # Obtener la lista de fuentes disponibles
    font_list = figlet.getFonts()

    # Solicitar al usuario el nombre de la fuente
    font_name = input("Ingrese el nombre de la fuente (deje en blanco para elegir aleatoriamente): ").strip()

    # Seleccionar una fuente aleatoria si no se proporciona ninguna
    if not font_name:
        font_name = random.choice(font_list)

    # Verificar si la fuente ingresada está disponible
    if font_name not in font_list:
        print("La fuente ingresada no está disponible. Seleccione una de las siguientes fuentes:")
        print(font_list)
        return

    # Solicitar al usuario el texto a imprimir
    text = input("Ingrese el texto a imprimir: ")

    # Establecer la fuente seleccionada
    figlet.setFont(font=font_name)

    # Imprimir el texto con la fuente seleccionada
    print(figlet.renderText(text))

if __name__ == "__main__":
    main()
