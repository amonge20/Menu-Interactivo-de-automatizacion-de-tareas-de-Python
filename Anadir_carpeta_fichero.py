# Importacion de los modulos de Python
import os, time

# Funcion para añadir carpeta o fichero
def crear_carpeta_fichero():
    print("\n ---- AÑADIR CARPETA O FICHERO ----")
    carpeta_o_fichero = input("¿Que quieres añadir? (Carpeta/Fichero)")

    # Para añadir carpeta
    if carpeta_o_fichero == "carpeta":
        Nombre_Carpeta = input("Nombre de la carpeta: ")
        try: 
            print("Creando carpeta...")
            time.sleep(2)
            os.mkdir(Nombre_Carpeta)
            print(f"Carpeta '{Nombre_Carpeta}' creada correctamente")
        except FileExistsError:
            print("Ya existe una carpeta con ese nombre")
            
    # Para añadir fichero
    elif carpeta_o_fichero == "fichero":
        Nombre_Fichero = input("Nombre del fichero: ")
        try: 
            print("Creando fichero...")
            time.sleep(2)
            with open(Nombre_Fichero,'w') as f:
                pass # Solo lo crea
        except FileExistsError:
            print("Ya existe una carpeta con ese nombre")