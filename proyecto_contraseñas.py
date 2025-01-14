import os
import re

contraseñas = []
patrones_obvios = []
resultados = []

BLUE = "\033[34m"
RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m" 
YELLOW = "\033[33m"

#Menu para el main
def mostrar_menu():
    print(BLUE + "\nMenú de opciones:" )
    print("1. Cargar archivos de contraseñas y patrones obvios")
    print("2. Calcular puntaje de seguridad y clasificar contraseñas")
    print("3. Ordenar contraseñas segun su puntaje de seguridad")
    print("4. Exportar resultados")
    print(RED + "5. Salir" + RESET)

def leer_contraseñas(archivo):
        #Limpiar arreglo para evitar repeticion de contraseñas en caso de cargar el archivo 2 veces
        contraseñas.clear
        if os.path.exists(archivo):
            with open(archivo, "r") as f:
                lineas = f.readlines()
                for i in range(0, len(lineas)):
                    contraseña = lineas[i].strip()
                    contraseñas.append(contraseña)

                print(GREEN + "\n Contraseñas cargados exitosamente\n" + RESET)
        else:
            print(RED + "Archivo de contraseñas no encontrado." + RESET)

def leer_patrones_obvios(archivo):
        #Limpiar arreglo para evitar repeticion de patrones obvios en caso de cargar el archivo 2 veces
        patrones_obvios.clear
        if os.path.exists(archivo):
            with open(archivo, "r") as f:
                lineas = f.readlines()
                for i in range(0, len(lineas)):
                    patron = lineas[i].strip()
                    patrones_obvios.append(patron)

                print(GREEN + "\n Patrones Obvios cargados exitosamente\n" + RESET)
        else:
            print(RED + "Archivo de Patrones Obvios no encontrado." + RESET)


def calcular_puntaje(contraseñas, patrones_obvios):
    if not contraseñas or not patrones_obvios:
        print(RED + "\nNo hay contraseñas ni patrones obvios almacenados." + RESET)
        return
    #Borrar los datos almacenados en el arreglo resultados por si se elige 2 veces la opcion de calcular puntaje 
    resultados.clear()

    #Bucle for para recorrer el arreglo en donde estan alamcenadas las contraseñas
    for contraseña in contraseñas:
        puntaje = 0
        simbolos_encontrados = 0
        
        #Sumar un punto por cada caracter
        puntaje += len(contraseña)
        
        #Sumar un punto si posee minusculas
        if re.search(r'[a-z]', contraseña):
            puntaje += 1
        
        #Sumar un punto si posee numeros
        if re.search(r'[0-9]', contraseña):
            puntaje += 1
        
        #Sumar un punto si posee MAYUSCULAS
        if re.search(r'[A-Z]', contraseña):
            puntaje += 1
        
        #Sumar 3 puntos si posee simbolos
        simbolos = re.findall(r'[^a-zA-Z0-9\s]', contraseña)
        if simbolos:
            puntaje += 3
            simbolos_encontrados = len(simbolos)
        
        #Sumar 2 puntos por cada simbolo adicional
        if simbolos_encontrados > 1:
            puntaje += (simbolos_encontrados - 1) * 2
        
        #Bucle for para verificar la contraseña posee algun patron obvio recorriendo el arreglo patrones Obvios
        for patron in patrones_obvios:
            if patron in contraseña :
                puntaje -= 5

        #Clasificacion de las contraseñas  
        if puntaje <= 15:
            clasificacion = "Débil"
        elif 16 <= puntaje <= 20:
            clasificacion = "Moderada"
        elif 21 <= puntaje <= 35:
            clasificacion = "Buena"
        elif 36 <= puntaje <= 100:
            clasificacion = "Excelente"
        else:
            clasificacion = "Impenetrable"
        
        #Añadir contraseña su puntaje y su clasificacion a otro arreglo
        resultados.append((contraseña, puntaje, clasificacion))
    
    print(GREEN + "\nCalculo del puntaje y claseificación de las contraseñas exitoso" + RESET)

    return resultados

# Implementación del algoritmo de ordenamiento de burbujas para ordenar los resultados de mayor a menor puntaje
def ordenar_contraseñas(resultados):
    if not contraseñas or not patrones_obvios:
        print(RED + "\nNo hay contraseñas ni patrones obvios almacenados." + RESET)
        return
    
    if not resultados:
        calcular_puntaje(contraseñas, patrones_obvios)


    n = len(resultados)
    for i in range(n):
        for j in range(0, n - i - 1):
            if resultados[j][1] < resultados[j + 1][1]:  
                resultados[j], resultados[j + 1] = resultados[j + 1], resultados[j]

    print(GREEN + "\nContraseñas ordenadas exitosamente" + RESET)

# Función para exportar los resultados a un archivo
def exportar_resultados(resultados):
    if not contraseñas or not patrones_obvios:
        print(RED + "\nNo hay contraseñas ni patrones obvios almacenados." + RESET)
        return  
    
    if not resultados:
        calcular_puntaje(contraseñas, patrones_obvios)
        ordenar_contraseñas(resultados)




    archivo_salida = "Resultados.txt"
    with open(archivo_salida, "w") as f:
        for contraseña, puntaje, clasificacion  in resultados:
            f.write(f"{contraseña} | {clasificacion} | {puntaje}\n")

    print(GREEN + f"\nArchivo '{archivo_salida}'  exportado exitosamente." + RESET)

# Programa principal con menú interactivo
def main():

    while True:
        mostrar_menu()
        # Solicitar la opción del usuario
        opcion = input(YELLOW + "Seleccione una opción (1-5): " + RESET)

        if opcion == '1':
            # Leer archivos
            leer_contraseñas("Contraseñas.txt")
            leer_patrones_obvios("Patronesobviosdecontraseña .txt")


        elif opcion == '2':
            # Calcular el puntaje de seguridad y clasificar las contraseñas
            calcular_puntaje(contraseñas, patrones_obvios)

        elif opcion == '3':
            # Ordenar las contraseñas según puntaje
            ordenar_contraseñas(resultados)

        elif opcion == '4':
            # Exportar los resultados a un archivo
            exportar_resultados(resultados)

        elif opcion == '5':
            # Salir del programa
            print(GREEN + "\nSaliendo del programa. ¡Hasta Luego!" + RESET)
            break

        else:
            print(RED + "Opción inválida. Por favor, seleccione una opción entre 1 y 5." + RESET)

if __name__ == "__main__":
    main()