

from tkinter import *
from tkinter import messagebox

class Principal():
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("afterexamen")
        self.ventana.geometry("500x600")
        self.ValidarNumeros = (
                self.ventana.register(self.Validarnumeros),"%P"                       
            )
    def  Validarnumeros(self,valor):
        return all(
            caracter.isnumeric()
            for caracter in valor 
        )

       
    def Disenio(self):
        Label(self.ventana, text="Pares y nones").place(x=200, y=5)
        Label(self.ventana, text="Escribe un numero").place(x=20, y=50)
        self.nombre = Entry(self.ventana, width=20,validatecommand= self.ValidarNumeros)
        self.nombre.place(x=150, y=50)
        self.ventana.mainloop()

if __name__=="__main__":
    app = Principal()
    app.Disenio()