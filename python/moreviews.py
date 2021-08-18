import os
import time
import platform
from colorama import Fore, Back, Style, init
init(autoreset=True)

sistema = platform.system()

if sistema == "Windows":
    os.system("cls")
    print()
    print(Fore.RED + "                                  .__                     \n  _____   ___________   _______  _|__| ______  _  ________\n /     \ /  _ \_  __ \_/ __ \  \/ /  |/ __ \ \/ \/ /  ___/\n|  Y Y  (  <_> )  | \/\  ___/\   /|  \  ___/\     /\___ \ \n|__|_|  /\____/|__|    \___  >\_/ |__|\___  >\/\_//____  >\n      \/                   \/             \/           \/ ")
    time.sleep(1.5)
    print()
    usuario = input(Fore.CYAN + "tu nombre de creador de contenido: ")
    print()
    print(Fore.CYAN + "perfecto " + usuario + " vamos a sumar visitas!")
    time.sleep(1)
    print()
    print(Fore.YELLOW + "-se recomienda usar una vpn")
    print(Fore.YELLOW + "-el unico navegador compatible es chrome hasta el momento")
    time.sleep(.8)
    print()
    link = input(Fore.LIGHTCYAN_EX + "link del video a sumar visitas: ")
    print()
    print(Fore.CYAN + "es posible que solo puedas sumar hasta 300 visitas,\nya estamos trabajando para arreglarlo")
    print()
    cant_visitas = int(input(Fore.GREEN + "cantidad limite de visitas que deseas recibir, recuerda lo de arriba: "))
    print()
    print(Fore.YELLOW + "cierra chrome, paresera que el programa se traba, solo dejalo correr asta que termine")
    print()
    tiempo_carga = float(input(Fore.CYAN + "cual es el tiempo de carga de la web\n(puedes abrir la web una vez y cronometrarlo)(solo segundos): "))
    visitas_hechas = int(0)
    while visitas_hechas < cant_visitas:
        os.system("start chrome /incognito " + link + "")
        visitas_hechas = visitas_hechas + int(1)
        time.sleep(tiempo_carga + 45)
        os.system("taskkill /F /IM chrome.exe /T > nul")
        time.sleep(3.5)
        print()
        if visitas_hechas == cant_visitas:
            print("terminado, se realizaron " + str(visitas_hechas) + " visitas exitosamente!")

if sistema == "Linux":
    os.system("clear")
    print("hola usuario, quieres recibir más visitas pero no sabes como, pues aqui tengo la solución")
    print()
    time.sleep(1.5)
    usuario = input("tu nombre de creador de contenido: ")
    print()
    print("perfecto " + usuario + " vamos a sumar visitas!")

if sistema != "Windows" and sistema != "Linux":
    print("su sistema no es soportado")
