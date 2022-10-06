import time as t

import pyautogui as pg, webbrowser as web


#archivo = input(" Ubicacion de archivo: ")
archivo = "numeros.txt"
#mensaje = input("Mensaje a enviar: ")
a = 0
with open(archivo) as file_object:
    for line in file_object:
        #leer = file_object.read()
        leer = file_object.readline()
        int(line)
        a += 1
        print(f'https://web.whatsapp.com/send?phone=+{line}{a}')
        t.sleep(1)