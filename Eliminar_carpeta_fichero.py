# Importacion de los modulos de Python
import os, time, shutil

# Funcion para eliminar carpeta o fichero
def eliminar_carpeta_fichero():
    print("\n ---- ELIMINAR CARPETA O FICHERO ----")
    carpeta_o_fichero = input("¿Que quieres eliminar? (Carpeta/Fichero)")

    # Para eliminar carpeta
    if carpeta_o_fichero == "carpeta":
        Nombre_Carpeta = input("Nombre de la carpeta que quieres eliminar: ")
        try: 
            print("Eliminando carpeta...")
            time.sleep(2)
            shutil.rmtree(Nombre_Carpeta)
            print(f"Carpeta '{Nombre_Carpeta}' eliminada correctamente")
        except FileNotFoundError:
            print("Ya se elimino esa carpeta")
            
    # Para eliminar fichero
    elif carpeta_o_fichero == "fichero":
        Nombre_Fichero = input("Nombre del fichero: ")
        try: 
            print("Eliminando fichero...")
            time.sleep(2)
            os.remove(Nombre_Fichero)
            print(f"Fichero '{Nombre_Fichero}' eliminada correctamente")
        except FileNotFoundError:
            print("Ya se elimino ese fichero")