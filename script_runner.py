
import subprocess
import sys
import os

if __name__ == '__main__':

    folder = 'scripts'

    while True:
        filename = input("Escribe el nombre del archivo de scripts/ que quieres ejecutar (sin .py): ")

        if os.path.join(folder, filename) == f'{folder}\{filename}':
            subprocess.run([sys.executable, '-m', f'{folder}.{filename}'])
        else:
            print("No se ha encontrado el archivo")

        if input("¿Quieres cerrar el script-runner? (s): ") == "s":
            break 

# El código tiene un error, si salta la excepción del os.path.join no hace el else de después. 
# Por lo demás, el código funciona perfectamente.