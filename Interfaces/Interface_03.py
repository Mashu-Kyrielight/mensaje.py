from tkinter import *
import os
raiz = Tk()

raiz.title("Principal")
raiz.geometry("805x502")
raiz.resizable(0,0)

colorletra = "#EB5353"


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


###################################### DENTRO DEL FRAME ####################################################

dirimgLabel=Label(miFrame, text="Direccion Imagen: ", bg="#2E4053",fg="white",font=12).place(x=50,y=40)
dirimgText=Entry(miFrame, font=12).place(x=190,y=40)

direxcelLabel=Label(miFrame, text="Direccion Excel: ", bg="#2E4053",fg="white",font=12).place(x=50,y=80)
direxcelText=Entry(miFrame, font=12).place(x=190,y=80)

mensajeLabel=Label(miFrame, text="Mensaje: ", bg="#2E4053",fg="white",font=12).place(x=50,y=120)
mensajeText=Entry(miFrame, font=12, fg=colorletra).place(x=190,y=120, width=200, height=100)

#passLabel=Label(miFrame, text="Contraseña: ", bg="#2E4053",fg="white",font=12).place(x=50,y=160)
#passText=Entry(miFrame, font=12, fg="black", show="*").place(x=190,y=160)

#comentarioLabel=Label(miFrame, text="Comentario: ", bg="#2E4053",fg="white",font=12).place(x=50,y=200)
#comentarioText=Entry(miFrame, font=12).place(x=190,y=200)



def abrir():
    os.system("start /B start cmd.exe @cmd /k netstat -ano")


click_iniciar=Button(miFrame, text="Iniciar",bg="#EB1D36",font=12, pady=10, padx=10, cursor="hand2").place(x=400,y=40)
click_open=Button(miFrame, text="Abrir cmd",bg="#000", fg="white" ,font=12, cursor="hand2", command=abrir).place(x=400,y=100)







raiz.mainloop()