# Importacion de los modulos de Python
import os, time, shutil

# Funcion para copiar carpeta o fichero
def copiar_carpeta_fichero():
    print("\n ---- COPIAR CARPETA O FICHERO ----")
    carpeta_o_fichero = input("¿Que quieres copiar? (Carpeta/Fichero)").strip().lower()

    # Para copiar carpeta
    if carpeta_o_fichero == "carpeta":
        Nombre_Carpeta_Origen = input("Ruta de la carpeta que quieres copiar: ").strip()
        Nombre_Carpeta_Destino = input("Ruta de destino con el nuevo nombre: ").strip()
        
        # Si la ruta no existe
        if not os.path.isdir(Nombre_Carpeta_Origen):
            print("La carpeta de origen no existe")
            return
        
        # Copiando carpeta
        try: 
            print("Copiando carpeta...")
            time.sleep(2)
            shutil.copytree(Nombre_Carpeta_Origen, Nombre_Carpeta_Destino)
            print(f"Carpeta copiada de '{Nombre_Carpeta_Origen}' a '{Nombre_Carpeta_Destino}'")
        except FileExistsError:
            print("Ya existe una carpeta con ese nombre en el destino.")
        except Exception as e:
            print(f"Error inesperado al copiar la carpeta: {e}")    
            
    # Para copiar fichero
    elif carpeta_o_fichero == "fichero":
        Nombre_Carpeta_Origen = input("Ruta de la carpeta que quieres copiar: ").strip()
        Nombre_Carpeta_Destino = input("Ruta de destino con el nuevo nombre: ").strip()
        
        # Copiando fichero
        try: 
            print("Copiando fichero...")
            time.sleep(2)
            shutil.copyfile(Nombre_Carpeta_Origen, Nombre_Carpeta_Destino)
            print(f"Fichero copiado de '{Nombre_Carpeta_Origen}' de '{Nombre_Carpeta_Destino}'")
        except Exception as e:
            print(f"Error al copiar el fichero: {e}")  