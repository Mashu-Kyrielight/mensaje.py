from io import open
import time as t
import pyautogui as pg, webbrowser as web

archivo = open("numeros.txt","r")


linea = archivo.readline(9)
a = 0
for i in archivo:
    a += 1
    print(linea)
    t.sleep(1)