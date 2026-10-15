
from tkinter import *
from tkinter import messagebox

class validar():
    def __init__(self):
        pass
        
    def Validarproducto(self, a):
        c = 0
        for i in a:
            if (ord(i) >=65 and ord(i)<=90) or (ord(i) >=97 and ord(i)<=122) or (ord(i)==32):
                c += 1
                if c == len(a):
                    return True
            else:
                messagebox.showerror("Error","Favor de ingresar un producto vaido")
                return False

    def Validarcantidad(self,valor):
            
            try:
                self.a = int(valor)
                return True
            except ValueError:
                messagebox.showerror("Error", "Favor de escribir correctamente la cantidad")
                return False

    def Validarprecio(self,valor):
        
                try:
                    self.a = float(valor)
                    return True
                except ValueError:
                    messagebox.showerror("Error", "Favor de escribir correctamente el precio")
                    return False
    
if __name__=="__main__":
     app= validar()
     app.Validarproducto()
     app.Validarprecio()
     app.Validarcantidad()