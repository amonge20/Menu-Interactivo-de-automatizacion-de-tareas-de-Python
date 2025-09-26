# Importación de los .py de los script
from Anadir_carpeta_fichero import crear_carpeta_fichero
from Eliminar_carpeta_fichero import eliminar_carpeta_fichero
from Copiar_carpeta_fichero import copiar_carpeta_fichero
from Mover_carpeta_fichero import mover_carpeta_fichero

# Bienvenido al programa de automatización
print("\n")
print("Hola, bienvenido al menu principal del Script de automatización de tareas de Python \n")

while True:
    # Selección multiple del menu interactivo
    print("\n --- MENU PRINCIPAL ---")
    print("1. Añadir carpeta o eliminar carpeta")
    print("2. Eliminar carpeta o eliminar fichero")
    print("3. Copiar carpeta o fichero")
    print("4. Mover carpeta o fichero")
    print("5. Salir")
    print("\n")
    print("Script creado por Aitor Monge Santiago")

    numero_Seleccionado = int(input("Por favor seleccione una opcion: "))

    if numero_Seleccionado == 1:
        crear_carpeta_fichero()
    elif numero_Seleccionado == 2:
        eliminar_carpeta_fichero()
    elif numero_Seleccionado == 3:
        copiar_carpeta_fichero()
    elif numero_Seleccionado == 4:
        mover_carpeta_fichero()
    else:
        print("Gracias por usar este programa. Adios")
        exit()
        break