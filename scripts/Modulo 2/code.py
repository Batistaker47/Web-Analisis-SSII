import subprocess
import json
import os

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def mostrar_menu():
    """
    Muestra el menú al usuario.
    """

    print("Bienvenido al script de ping.")
    print("¿Qué desea hacer?")
    print("1. Ejecutar el código")
    print("2. Acceder a la documentación")
    print("3. Exportar resultados")
    print("4. Salir")


def obtener_opcion():
    """
    Obtiene la opción del usuario del menú.

    Returns:
        La opción del usuario.
    """
    opcion = input("Introduzca una opción: ")
    while opcion not in ("1", "2", "3", "4"):
        print("Opción no válida.")
        opcion = input("Introduzca una opción: ")
    return opcion


def ejecutar_codigo():
    """
    Ejecuta el código del script.
    """
    ip = "192.168.128"
    print("Escaneando las IP's desde la : " + ip + ".1 hasta la " + ip + ".255")

    subnet = ip.split(".")

    FNULL = open(os.devnull, 'w')

    for x in range(1, 255):
        ip2 = subnet[0] + "." + subnet[1] + "." + subnet[2] + "." + str(x)
        response = subprocess.Popen(["ping", "-n", "1", ip2], stdout=FNULL, stderr=subprocess.STDOUT).wait()
        if response == 0:
            print(bcolors.OKGREEN + ip2, 'está viva!' + bcolors.ENDC)
        else:
            print(bcolors.FAIL + ip2, 'está muerta!' + bcolors.FAIL)

def acceder_a_documentacion():
    """
    Muestra la documentación.
    """
    print("Documentacion del programa:"
          """
          Este script se puede utilizar para buscar los equipos que estan vivos de la red 192.168.128.0.
          La implementación para la búsqueda de las subredes no se ha logrado conseguir a pesar de los esfuerzos.
          Aun así, se ha logrado una interfaz bastante competente, y que muestra los equipos que generan respuesta a los ping
          """
          )


def exportar_resultados():
    """
    Exporta los resultados del ping a un documento en formato JSON.
    resultados = []

    """
    print("Exportando datos, espere unos minutos...")
    subprocess.call("escaneoExportar.cmd")
    with open("sample.txt", "r") as f:
        results = f.readlines()

    results_json = [json.loads(line) for line in results]

    with open("results.json", "w") as f:
        json.dump(results_json, f)


    print("¡Los resultados han sido exportados con éxito!")


def salir():
    """
    Sale del programa.
    """


mostrar_menu()
opcion = obtener_opcion()

while opcion != "4":
    if opcion == "1":
        ejecutar_codigo()
    elif opcion == "2":
        acceder_a_documentacion()
    elif opcion == "3":
        exportar_resultados()
    mostrar_menu()
    opcion = obtener_opcion()

print("¡Hasta la próxima!")
