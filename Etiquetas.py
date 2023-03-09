from tkinter import *
from tkinter import ttk

raiz = Tk()
etqTexto = ttk.Label(raiz, text="Itachi modo MIAUU")
etqTexto.grid()

imagen = PhotoImage(file="miau.png")

etqImagen = ttk.Label(raiz)
etqImagen.grid()
etqImagen['image']=imagen

etqCombinada =ttk.Label(raiz, text="DIOS ITACHII", compound="center")
etqCombinada.grid()
etqCombinada['image']=imagen

raiz.mainloop()