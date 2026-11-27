
from tkinter import messagebox
import json
import os

archivo = "otrodatos.json"

class Principal():
    def __init__(self):
        if not os.path.exists(archivo):
            with open(archivo, "w", encoding="utf-8") as f:
                json.dump([], f, indent=4, ensure_ascii=False)
        else:
            messagebox.showinfo("Mensaje", "El archivo ya existe")

        self.op = 0
        self.datos = []
        self.menu()

    def menu(self):

        self.precargardatos()

        print(f"\nEl archivo tiene {len(self.datos)} elementos")
        print("1.- Agregar")
        print("2.- Mostrar")
        print("3.- Eliminar")
        print("4.- Salir")

        self.op = int(input("Escribe una opcion: "))

        if self.op == 1:
            nombre = input("Escribe un nombre: ")
            edad = input("Escribe la edad: ")

            estruc = {
                "Nombre": nombre,
                "Edad": edad
            }

            self.datos.append(estruc)

            with open(archivo, "w", encoding="utf-8") as f:
                json.dump(self.datos, f, indent=4, ensure_ascii=False)

            print("Datos guardados")
            self.menu()

        elif self.op == 2:
            self.mostrar()
            self.menu()

        elif self.op == 3:
            self.eliminar()
            self.menu()

        elif self.op == 4:
            print("Fin")

        else:
            print("Error, introduce una opcion valida")
            self.menu()

    def precargardatos(self):

        with open(archivo, "r", encoding="utf-8") as f:
            datos = json.load(f)

        if isinstance(datos, dict):
            self.datos = [datos]
        else:
            self.datos = datos

    def mostrar(self):

        if len(self.datos) == 0:
            print("No hay datos guardados")
        else:
            for i, d in enumerate(self.datos, start=1):
                print(f"\nRegistro {i}")
                print(f"Nombre: {d['Nombre']}")
                print(f"Edad: {d['Edad']}")

    def eliminar(self):

        self.mostrar()

        if len(self.datos) > 0:
            num = int(input("Escribe el numero del registro a eliminar: "))

            if num >= 1 and num <= len(self.datos):
                self.datos.pop(num - 1)

                with open(archivo, "w", encoding="utf-8") as f:
                    json.dump(self.datos, f, indent=4, ensure_ascii=False)

                print("Registro eliminado")
            else:
                print("Numero de registro no valido")


if __name__ == '__main__':
    app = Principal()

    