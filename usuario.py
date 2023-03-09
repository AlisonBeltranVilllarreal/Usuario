#app para ingresar un usuario y contraseña.
#Beltran Alison Judith
#3 Marzo 2023.

from tkinter import*
from tkinter import ttk


class usuario:
     def __init__(self, raiz):

        raiz.title("Inicio de Sesion")
        
        self.usuario=StringVar()
        self.contraseña=StringVar()

        mainFrame=ttk.Frame(raiz, padding="10 10 10 10")
        mainFrame.grid(column=0, row=0)

        usuarioEntry=ttk.Entry(mainFrame, textvariable=self.usuario)
        usuarioEntry.grid(column=1, row=1, columnspan=2)
        print(" ")
        contraseñaEntry=ttk.Entry(mainFrame, textvariable=self.contraseña)
        contraseñaEntry.grid(column=1, row=2, columnspan=2)


        ttk.Label(mainFrame, text="Usuario: \n").grid(column=0, row=1)
        print(" ")
        ttk.Label(mainFrame, text="Contraseña: \n").grid(column=0, row=2)
        print(" ")
        ttk.Button(mainFrame, text="Ingresar").grid(column=2,row=3)
        
        #Hacer que funcione con enter
        raiz.bind("<Return>", self.ingresar)

     def ingresar(self, *args):
        print("Boton Presionado")
        datoUsuario = float(self.get())
        print("Usuario Ingresado: ", datoUsuario)
        Contraseña = float(self.get())
        print("Contraseña: ", Contraseña)
        