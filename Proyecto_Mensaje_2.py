import pyautogui as pg
import webbrowser as web
import time as t
import pandas as pd
#from pandas import options
##########
#from selenium import webdriver
#driver_path = "C:\dchrome\chromedriver.exe"
#driver = webdriver.Chrome(driver_path, chrome_options = options)
#imagen = "C:\Users\elhab\Desktop\GENERAL LEARNING\Practice_Python\Learning_A\Proyecto_Mensaje\cat.jpg"
##########
data = pd.read_csv("Numeros.csv")
data_dict = data.to_dict('list')
phono = data_dict['Numero']
sms = data_dict['Mensaje']
combo = zip(phono,sms)
first = True
for phono,sms in combo:
    t.sleep(5)
    web.open(f'https://web.whatsapp.com/send?phone={phono}&text={sms}')
    if first:
        t.sleep(8)
        first = False
    width,height = pg.size()
    pg.click(width/2,height/2)
    t.sleep(5)
    pg.press('enter')
    t.sleep(6)
    pg.hotkey('ctrl', 'w')
