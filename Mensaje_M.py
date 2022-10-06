#with open("numeros.txt") as file_object:
#    leer = file_object.read()
#    print(leer)
import time as t

import pyautogui as pg, webbrowser as web


#archivo = input(" Ubicacion de archivo: ")
archivo = "numeros.txt"
#mensaje = input("Mensaje a enviar: ")

with open(archivo) as file_object:
    for line in file_object:
        leer = file_object.readline()
        #print(line)
        int(line)
        #t.sleep(1)
        web.open(f'https://web.whatsapp.com/send?phone=+{line}')
        t.sleep(10)
        pg.write("este es un mensaje de prueva")
        pg.press('enter')
        pass
        t.sleep(5)
        #print(f'https://web.whatsapp.com/send?phone=+{line}')
        #t.sleep(1)
        pg.hotkey('ctrl', 'w')
        t.sleep(2)