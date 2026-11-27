
from tkinter import *
from tkinter import messagebox
import re

class Principal():
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("Programa 1 Parcial 3")
        self.ventana.geometry("400x300")
        self.validar_nombre = (
            self.ventana.register(self.validar_letrasyespacios),"%P"                       
        )
        self.validar_edad = (
                    self.ventana.register(self.validar_numeros),"%P"                       
                )
        
    def validar_numeros(self, valor):
        return all(
            caracter.isnumeric()
            for caracter in valor
        )
    
    def validar_letrasyespacios(self,valor):
        return all(
            caracter.isalpha() or caracter.isspace()
            for caracter in valor
        )
    def Agregar(self):
        nombre = self.nombre.get()
        Edad = self.edad.get()
        if len(nombre)==0 or len(Edad)==0:
            messagebox.showerror("Error", "Faltan datos por agregar")
        else:
            self.lista.insert(
                END,
                f'{nombre:<25}{Edad:<5}'
            )
            self.nombre.delete(0,END)
            self.edad.delete(0,END)

    def Disenio(self):
        Label(self.ventana, text="Practicas del tercer parcial").place(x=120 ,y=5)
        Label(self.ventana, text="Escribre un nombre").place(x=50, y=25)
        self.nombre = Entry(self.ventana, validate="key", width=25, validatecommand= self.validar_nombre)
        self.nombre.place(x=50 ,y=50)
        Label(self.ventana, text="Escribre la edad").place(x=50, y=70)
        self.edad = Entry(self.ventana, validate="key", width=25, validatecommand= self.validar_edad)
        self.edad.place(x=50, y=90)
        self.lista = Listbox(self.ventana, height= 8, width=25, activestyle="dotbox")
        self.lista.place(x=240, y=50)
        # self.lista.insert(
        #     END,
        #     f'{'Nombre                 '}{'Edad                   '}'
        # )
        # self.lista.insert(
        #     END,
        #     f'{'******************************************************'}'
        # )
        self.lista.insert(
            END,
            f'{'Nombre':<25}{'Edad':<5}'
        )
        self.lista.insert(
            END,
            "*"*50
        )
        Button(self.ventana, text="Agregar", command=self.Agregar).place(x=50 ,y=125)
        self.ventana.mainloop()

if __name__=='__main__':
    app = Principal()
    app.Disenio()