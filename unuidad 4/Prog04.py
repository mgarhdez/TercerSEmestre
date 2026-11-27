
from tkinter import *
from tkinter import messagebox
import re 
import os
import json
archivo  = "Agenda.json"
class Principal():
    def __init__(self):
        if not os.path.exists(archivo):
            with open(archivo, "w", encoding="utf-8") as f:
                json.dump([], f, indent=4, ensure_ascii=False)
        else:
            messagebox.showinfo("Error","El archivo ya existe")
                
        self.ventana = Tk()
        self.ventana.title("Programa 4 Parcial 3")
        self.ventana.geometry("600x300")
        self.validar_edad = (
            self.ventana.register(self.validar_numeros_enteros),"%P"                       
                )
        self.validar_nombre = (
            self.ventana.register(self.validar_letras_espacios), "%P"
        )
        self.validar_telefono = (
            self.ventana.register(self.validar_telefono_len),"%P"
        )

    def validar_numeros_enteros(self,valor):
        return all(
            caracter.isnumeric()
            for caracter in valor
        )
    def validar_letras_espacios(self, valor):
        return all(
            caracter.isalpha() or caracter.isspace()
            for caracter in valor
        )
    
    def validar_telefono_len(self, valor):
        return len(valor)<=10 and all(
            caracter.isnumeric()
            for caracter in valor

        )
    
    def Disenio(self):
        Label(self.ventana, text="Practica 4 Parcial3",
            font=("Arial", 16, "bold")).place(x=100, y=5)
        Label(self.ventana, text="Escribe el nombre",
            font=("Arial", 8, "bold")).place(x=100, y=50)
        self.nombre = Entry(self.ventana, validate="key", validatecommand= self.validar_nombre)
        self.nombre.place(x=210, y=50)
        Label(self.ventana, text="Escribe la edad",     
            font=("Arial", 8, "bold")).place(x=100, y=75)
        self.edad = Entry(self.ventana, validate="key", validatecommand=self.validar_edad)
        self.edad.place(x=210, y=75)
        Label(self.ventana, text="Escribe el telefono",
            font=("Arial", 8, "bold")).place(x=100, y=100)
        self.telefono = Entry(self.ventana, validate="key", validatecommand=self.validar_telefono,)
        self.telefono.place(x=210, y=100)
        self.lista = Listbox(
            self.ventana,
            width=75,
            height=10,
            font=("Consolas",10),
            activestyle="dotbox"
        )
        self.lista.place(x=20,y=130)
        Button(self.ventana, text="Agregar",width=10, command=self.agregar).place(x=390,y=75)
        Button(self.ventana, text= "Salir", width=10,command= self.salir).place(x=390, y=45)

    def salir(self):
        self.ventana.destroy()


    def agregar(self):
        nombre = self.nombre.get()
        edad = self.edad.get()
        telefono = self.telefono.get()
        if len(nombre)==0 or len(edad)==0 or len(telefono)==0:
            messagebox.showerror("Error","Faltan datos")
            
        else:
            if len(telefono)==10:
                with open(archivo, "r",encoding="utf-8") as ar:
                    informacion = json.load(ar)
                if isinstance(informacion, dict):
                    informacion = [informacion]

                estructura = {
                    "Nombre": nombre,
                    "Edad": edad,
                    "Telefono": telefono
                }
                
                informacion.append(estructura)

                with open(archivo, "w", encoding="utf-8")as ar:
                    json.dump(
                        informacion,
                        ar,
                        indent=4,
                        ensure_ascii= False
                    )
                messagebox.showinfo("Mensaje", "Datos aguardados correctamente")
                self.nombre.delete(0,END)
                self.edad.delete(0,END)
                self.telefono.delete(0,END)
                self.mostrar()
            else:
                messagebox.showerror(
                    "Error",
                    "agregar un telefono valido"
                )
           


    def mostrar(self):
        self.lista.delete(0,END)
        titulos = (
            f"{"ID":<8}"
            f"{"Nombre":<25}"
            f"{"Edad":<15}"
            f"{"Telefono"}"
        )
        self.lista.insert(END, titulos)
        separador = ("_"*100)
        self.lista.insert(END,separador)
        with open(archivo, "r",encoding="utf-8") as ar:
            informacion = json.load(ar)
        if isinstance(informacion, dict):
            informacion = [informacion]
        for i, d in enumerate(informacion, start=1):
            datos = (
                f"{i:<8}"
                f"{d["Nombre"]:<25}"
                f"{d["Edad"]:<15}"
                f"{d["Telefono"]:<25}"
            )
            self.lista.insert(END, datos)


if __name__=='__main__':
    app = Principal()
    app.Disenio()
    app.mostrar()
    app.ventana.mainloop()