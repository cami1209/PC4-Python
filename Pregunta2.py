import random
from pyfiglet import Figlet

def main():
    figlet = Figlet()

    font_list = figlet.getFonts()

    font_name = input("Ingrese el nombre de la fuente (deje en blanco para elegir aleatoriamente): ").strip()

    if not font_name:
        font_name = random.choice(font_list)

    if font_name not in font_list:
        print("La fuente ingresada no está disponible. Seleccione una de las siguientes fuentes:")
        print(font_list)
        return

    text = input("Ingrese el texto a imprimir: ")

    figlet.setFont(font=font_name)

    print(figlet.renderText(text))

if __name__ == "__main__":
    main()
