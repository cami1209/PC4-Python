def guardar_tabla_multiplicar(numero):
    try:
        with open(f"tabla-{numero}.txt", "w") as file:
            for i in range(1, 11):
                file.write(f"{numero} x {i} = {numero*i}\n")
        print(f"Tabla de multiplicar del {numero} guardada en tabla-{numero}.txt")
    except IOError:
        print("Error al intentar guardar la tabla de multiplicar.")

def mostrar_tabla_multiplicar(numero):
    try:
        with open(f"tabla-{numero}.txt", "r") as file:
            tabla = file.read()
            print(tabla)
    except FileNotFoundError:
        print(f"El archivo tabla-{numero}.txt no existe.")

def mostrar_linea_tabla(numero, linea):
    try:
        with open(f"tabla-{numero}.txt", "r") as file:
            lineas = file.readlines()
            if len(lineas) >= linea:
                print(lineas[linea - 1])
            else:
                print(f"No existe la línea {linea} en la tabla-{numero}.txt")
    except FileNotFoundError:
        print(f"El archivo tabla-{numero}.txt no existe.")

def menu():
    while True:
        print("\nMENU:")
        print("1. Guardar tabla de multiplicar")
        print("2. Mostrar tabla de multiplicar")
        print("3. Mostrar línea de la tabla de multiplicar")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            numero = int(input("Ingrese un número entre 1 y 10: "))
            if 1 <= numero <= 10:
                guardar_tabla_multiplicar(numero)
            else:
                print("El número debe estar entre 1 y 10.")
        elif opcion == "2":
            numero = int(input("Ingrese un número entre 1 y 10: "))
            if 1 <= numero <= 10:
                mostrar_tabla_multiplicar(numero)
            else:
                print("El número debe estar entre 1 y 10.")
        elif opcion == "3":
            numero = int(input("Ingrese un número entre 1 y 10: "))
            linea = int(input("Ingrese el número de línea a mostrar: "))
            if 1 <= numero <= 10 and linea >= 1:
                mostrar_linea_tabla(numero, linea)
            else:
                print("El número debe estar entre 1 y 10, y la línea debe ser mayor o igual a 1.")
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

menu()
