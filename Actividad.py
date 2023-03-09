from tkinter import *
from tkinter import ttk

class Actividad:
     def __init__(self, raiz):

        raiz.title("Muestra Widgets")
        
        self.Nombre=StringVar()
        self.APaterno=StringVar()
        self.AMaterno=StringVar()
        self.Correo=StringVar()
        self.Movil=StringVar()

        mainFrame=ttk.Frame(raiz, padding="10 10 10 10", relief="raised")
        mainFrame.grid(column=0, row=0)

        usuarioFrame=ttk.Frame(mainFrame,padding="10 10 10 10", relief="raised")
        usuarioFrame.grid(column=0, row=0, columnspan=2, rowspan=3)

        NombreEntry=ttk.Entry(usuarioFrame, textvariable=self.Nombre)
        NombreEntry.grid(column=1, row=1, columnspan=2)
        print(" ")
        APaternoEntry=ttk.Entry(usuarioFrame, textvariable=self.APaterno)
        APaternoEntry.grid(column=1, row=2, columnspan=2)
        print(" ")
        AMaternoEntry=ttk.Entry(usuarioFrame, textvariable=self.AMaterno)
        AMaternoEntry.grid(column=1, row=3, columnspan=2)
        print(" ")
        CorreoEntry=ttk.Entry(usuarioFrame, textvariable=self.Correo)
        CorreoEntry.grid(column=1, row=4, columnspan=2)
        print(" ")
        MovilEntry=ttk.Entry(usuarioFrame, textvariable=self.Movil)
        MovilEntry.grid(column=1, row=5, columnspan=2)

        ttk.Label(usuarioFrame, text="Nombre: \n").grid(column=0, row=1)
        ttk.Label(usuarioFrame, text="A. Paterno: \n").grid(column=0, row=2)
        ttk.Label(usuarioFrame, text="A. Materno: \n").grid(column=0, row=3)
        ttk.Label(usuarioFrame, text="Correo: \n").grid(column=0, row=4)
        ttk.Label(usuarioFrame, text="Movil: \n").grid(column=0, row=5)
        
        aficionesFrame=ttk.Frame(mainFrame, padding="10 10 10 10", relief="raised")
        aficionesFrame.grid(column=0, row=4, columnspan=2)

        ttk.Label(aficionesFrame, text="Aficiones: \n").grid(column=0, row=0)
        
        check = ttk.Checkbutton(aficionesFrame, text='Leer').grid(column=0, row=1)
        check = ttk.Checkbutton(aficionesFrame, text= 'Musica').grid(column=1, row=1)
        check = ttk.Checkbutton(aficionesFrame, text= 'Videojuegos').grid(column=2, row=1)

        personaFrame=ttk.Frame(mainFrame, padding="10 10 10 10")
        personaFrame.grid(column=2, row=0, rowspan=3)

        personita=StringVar()
        estudiante= ttk.Radiobutton(personaFrame, text='Estudiante',variable=personita, value='estudiante').grid(column=0,sticky=W)
        empleado= ttk.Radiobutton(personaFrame, text='Empleado',variable=personita, value='empleado').grid(column=0,sticky=W)
        desempleado= ttk.Radiobutton(personaFrame, text='Desempleado',variable=personita, value='desempleado').grid(column=0, sticky=W)

        comboFrame=ttk.Frame(mainFrame, padding="10 10 10 10")
        comboFrame.grid(column=2,row=4)

        estados = StringVar()

        comboEstados = ttk.Combobox(comboFrame, textvariable= estados)
        comboEstados.grid()
        comboEstados['values']=("Jalisco","Nayarit", "Colima", "Michoacan","Estados(32)")

        ttk.Button(mainFrame, text="Guardar").grid(column=0,row=5)
        ttk.Button(mainFrame, text="Cancelar").grid(column=1,row=5)