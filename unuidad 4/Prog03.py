

from tkinter import messagebox
import json
import os
archivo = "datos.json"

class Principal():
    def __init__(self): 
        if not os.path.exists(archivo):
            with open(archivo, "w", encoding="utf-8") as f:
                json.dump([], f, indent=4, ensure_ascii=False)
        else:
            messagebox.showinfo("Error","El archivo ya existe")
        
    def Agregar(self):    
        with open(archivo, "r", encoding="utf-8") as f:
            datos = json.load(f)
        if isinstance(datos, dict):
            datos = [datos]
        if len(datos)==0:
            messagebox.showinfo("Mensaje", "El archivo esta vacio")
        else:
            for i, d in enumerate(datos, start= 1):
                print(f'Nombre{d['nombre']}')
                print(f'Edad{d['edad']}')
                print(f'Telefono{d['Telefono']}')

        res = input("Deseas agregar otro elemento")
        if res == 's' or res =='si' or res =='Si' or res=='SI' or res=='sI':
            nombre = input("Escribe el nombre \n")
            edad = input("Escribe la edad \n")
            Telefono = input("Escribe el Telefono \n")
            estructura = {
                'nombre': nombre,
                'edad': edad,
                'Telefono': Telefono
            }
            datos.append(estructura)
            with open(archivo,"w", encoding="utf-8") as f:
                json.dump(datos, f, indent=4, ensure_ascii=False)
            messagebox.showinfo("Mensaje", "Los datos fueron guardados")
        re= input("Deseas salir del programa")
        if re == 's' or re =='si' or re =='Si' or re=='SI' or re=='sI':
            print('Fin')
        else:
            return self.Agregar()



if __name__=="__main__":
    app = Principal()
    app.Agregar()