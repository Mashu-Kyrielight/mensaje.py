from tkinter import *
import os
raiz = Tk()

raiz.title("Principal")
raiz.geometry("805x502")
#raiz.resizable(0,0)

############################# CENTRAR VENTANA ####################################
wtotal = raiz.winfo_screenwidth()
htotal = raiz.winfo_screenheight()
wventana = 805
hventana = 502
pwidth = round(wtotal/2-wventana/2)
pheight = round(htotal/2-hventana/2)
raiz.geometry(str(wventana)+"x"+str(hventana)+"+"+str(pwidth)+"+"+str(pheight))
##################################################################################


miFrame=Frame(raiz, width=800, height=500, bg="#2E4053")
miFrame.pack()

aaaaText=Text(miFrame, width=100, height=80, bg="black", fg="white")
aaaaText.grid(row=4, column=4, sticky="n", padx=10, pady=10)
aaaaText.config(width=30, height=10)

###################################### DENTRO DEL FRAME ####################################################

dirimgLabel=Label(miFrame, text="Direccion Imagen: ", bg="#2E4053",fg="white",font=12).place(x=50,y=40)
dirimgText=Entry(miFrame, font=12).place(x=190,y=40)




mensaje2Label=Label(miFrame, text="Mensaje 2: ", bg="#2E4053",fg="white",font=12).place(x=50,y=250)
aaaaText.grid(row=1, column=0, sticky="e", padx=10, pady=10)





click_iniciar=Button(miFrame, text="Iniciar",bg="#EB1D36",font=12, pady=10, padx=10, cursor="hand2").place(x=400,y=40)








raiz.mainloop()