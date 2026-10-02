try:
    archivo = open("mi_archivo.txt", "r")
    print(archivo.read())
    archivo.close()
except FileNotFoundError:
    print("Error: El archivo no existe. Lo voy a crear." )
    with open("mi_archivo.txt", "w") as archivo:
        archivo.write("Hola Gabriela, este archivo fue creado. ")
    print("Archivo creado con éxito.")



