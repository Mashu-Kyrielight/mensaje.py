from tkinter import *
import tkinter as tk

root = Tk()


miFrame = Frame(root, width=500, height=400)
miFrame.pack()

#miImagen=PhotoImage(file="D:\Chira_Mis_Recuerdos\_Anime\__Genshin Impact\npc.jpg")


Label = Label(miFrame, text="soy un label", fg="#212F3D", font=12).place(x=10, y=50)
#Label(miFrame, image=miImagen).place(x=100, y=200)

root.mainloop()
