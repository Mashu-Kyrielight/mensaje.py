from   tkinter import *
raiz = Tk()

raiz.title("Principal")
raiz.geometry("805x502")
raiz.resizable(0,0)

## CENTRAR LA VENTANA
wtotal = raiz.winfo_screenwidth()
htotal = raiz.winfo_screenheight()
wventana = 805
hventana = 502
pwidth = round(wtotal/2-wventana/2)
pheight = round(htotal/2-hventana/2)
raiz.geometry(str(wventana)+"x"+str(hventana)+"+"+str(pwidth)+"+"+str(pheight))


miFrame=Frame(raiz, width=800, height=500, bg="#2E4053")

miFrame.pack()






dirimgLabel=Label(miFrame, text="Direccion Imagen: ", bg="#2E4053",fg="white",font=12).place(x=50,y=40)
dirimgText=Entry(miFrame, font=12).place(x=200,y=40)

direxcelLabel=Label(miFrame, text="Direccion Excel: ", bg="#2E4053",fg="white",font=12).place(x=50,y=80)
direxcelText=Entry(miFrame, font=12).place(x=200,y=80)

click_iniciar=Button(miFrame, text="Iniciar",bg="#EB1D36",font=12).place(x=400,y=40)








raiz.mainloop()