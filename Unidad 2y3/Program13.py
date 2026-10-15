

from tkinter import *
from tkinter import messagebox
import time
from Validacion13 import validar
class Principal():
    def __init__(self):
        self.ventana = Tk()
        self.ventana.geometry("600x400")
        self.ventana.title("Practica 13")
        self.dato = ""
        self.pr = ""
        self.cant = ""
        self.pro = ""
        self.val = validar()
    def agregar(self):
        self.pr = self.precio.get()
        self.pro = self.producto.get()
        self.cant = self.cantidad.get()
        if len(self.pr)==0 or len(self.pro)==0 or len(self.cant)==0:
            messagebox.showerror("Error","No se ingresaron caracteres")
        else:
            if self.val.Validarproducto(self.pro): 
                if self.val.Validarcantidad(self.cant): 
                    if self.val.Validarprecio(self.pr):
                        self.dato = self.producto.get()+" _ "+self.precio.get()+" _ "+self.cantidad.get()+" _ "+(str(float(self.precio.get())*int(self.cantidad.get())))
                        self.lista.insert(self.lista.size()+1,self.dato)
                        self.producto.delete(0,END)
                        self.precio.delete(0,END)
                        self.cantidad.delete(0,END)
                        messagebox.showinfo("Correcto","Producto agregado")
                    else:
                        messagebox.showerror("Error", "al esribir el precio")
                        self.precio.delete(0,END)
                else:
                    messagebox.showerror("Error", "error al esribir la cantidad")
                    self.cantidad.delete(0,END)
            else:
                messagebox.showerror("Error", " error al esribir el producto")
                self.producto.delete(0,END)
       

    def elegir(self):
        seleccion = self.lista.curselection()
        if not seleccion:
             messagebox.showerror("Error","Primero elige un elemento")
        else:
                renglon = self.lista.get(seleccion[0])
                print(renglon)
                r = renglon.split(" _ ")
                messagebox.showinfo("Ventana",f"El producto es {r[0]}\n y el precio es: {r[1]}\n" +
                                    f" la cantidad es: {r[2]} \n y el total es:{r[3]}")
                
    def eliminar(self):
        seleccion = self.lista.curselection()
        if not seleccion:
            messagebox.showerror("Error","Primero elige un elemento")
        else:
            indice = seleccion[0]
            self.lista.delete(indice)
            messagebox.showinfo("Eliminar","El dato ha sido eliminado")
         
    def Cerrar(self):
         self.ventana.destroy()

    def Disenio(self): 
        Label(self.ventana, text= 'Programa 13',
            font=("Times New Roman",18, "bold")).place(x=100,y=5) 
        Label(self.ventana, text= "Escribe un producto").place(x=20,y=50)
        self.producto = Entry(self.ventana)
        self.producto.place(x=20,y=70)
        Label(self.ventana, text= "Escribe un precio").place(x=20,y=95)
        self.precio = Entry(self.ventana)
        self.precio.place(x=20,y=115)
        Label(self.ventana, text= "Escribe la cantidad de productos").place(x=20,y=140)
        self.cantidad = Entry(self.ventana)
        self.cantidad.place(x=20,y=165)
        self.lista = Listbox(self.ventana, height=15, width=30, activestyle="dotbox")
        self.lista.place(x=240, y=50)
        Button(self.ventana, text="Agregar",command=self.agregar).place(x=165, y=30)
        Button(self.ventana, text="Seleccionar",command=self.elegir).place(x=165, y=57)
        Button(self.ventana, text="Eliminar",command=self.eliminar).place(x=165, y=85)
        Button(self.ventana, text="Cerrar",command=self.Cerrar).place(x=165, y=115)
       
        self.ventana.mainloop()

if __name__=='__main__':
    app= Principal()
    app.Disenio()