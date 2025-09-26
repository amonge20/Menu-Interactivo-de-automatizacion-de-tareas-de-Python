# Importacion de los modulos de python
import os, shutil, time

# Funcion para mover ficheros y carpetas
def mover_carpeta_fichero():
    print("\n ---- MOVER CARPETA O FICHERO ----")
    tipo = input("¿Qué quieres mover? (carpeta/fichero): ").strip().lower()

    # Incluimos el nombre original + el de destino segun si hemos escrito carpeta o fichero
    origen = input("Ruta del archivo o carpeta de origen: ").strip()
    destino = input("Ruta de destino (incluye el nuevo nombre si quieres): ").strip()

    if tipo == "carpeta":
        if not os.path.isdir(origen):
            print("La carpeta de origen no existe.")
            return
    elif tipo == "fichero":
        if not os.path.isfile(origen):
            print("El fichero de origen no existe.")
            return
    else:
        print("Opción no válida. Debe ser 'carpeta' o 'fichero'.")
        return

    # Moviendo carpeta o fichero
    try:
        print("Moviendo...", end=" ")
        time.sleep(1)
        shutil.move(origen, destino)
        print(f"{tipo.capitalize()} movido de '{origen}' a '{destino}'")
    except Exception as e:
        print(f"Error al mover: {e}")