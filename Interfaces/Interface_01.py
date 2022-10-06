from tkinter import *
# raiz
#   frame
#       widges (conponentes - botones, etc)
tk = Tk()
# titulo
tk.title("Mi Interfaz Python")


# para inpedir que se modifique el tamaño de la ventana
#           width - height
tk.resizable(True,True)

tk.iconbitmap("D:\Chira_Mis_Recuerdos\_Anime\__Genshin Impact\___Genshin_Icon2.ico")

# tamaño o dimencion de ventana
tk.geometry("650x450")

# color fondo
tk.config(bg="orange")


# creando frame
miFrame=Frame()
miFrame.pack() # importante enpaquetar
#miFrame.pack(side="right")
#miFrame.pack(side="left")
#miFrame.pack(side="bottom")

miFrame.config(bg="grey")
miFrame.config(width="450", height="250")


# ubicando con puntos cardinales (norte, sur, este, oeste)
#miFrame.pack(side="left", anchor="n")
#miFrame.pack(side="right", anchor="s")
#miFrame.pack(side="bottom", anchor="e")
#miFrame.pack(side="right", anchor="w")

# expande con la raiz
miFrame.pack(fill="both", expand="True")
# se ajusta al medio
miFrame.pack(fill="y", expand="True")



# tamaño del  borde
miFrame.config(bd=10)
# borde
miFrame.config(relief="groove")


# cambiar forma del curso al pasa x el frame
miFrame.config(cursor="hand2")





# siempre ponerlo al ultimo
tk.mainloop()















#estudiar
# libreria de metodos para interfaz
# https://python.readthedocs.io/en/stable/library/tk.html