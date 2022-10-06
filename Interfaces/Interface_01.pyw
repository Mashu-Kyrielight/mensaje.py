from tkinter import *
# raiz
#   frame
#       widges (conponentes - botones, etc)
rz = Tk()
# titulo
rz.title("Mi nueva interfaz")


# para inpedir que se modifique el tamaño de la ventana
#           width - height
rz.resizable(True,True)

rz.iconbitmap("D:\Chira_Mis_Recuerdos\_Anime\__Genshin Impact\___Genshin_Icon2.ico")

# tamaño o dimencion de ventana
rz.geometry("650x350")

# color fondo
rz.config(bg="orange")



# siempre ponerlo al ultimo
rz.mainloop()















#estudiar
# libreria de metodos para interfaz
# https://python.readthedocs.io/en/stable/library/tk.html