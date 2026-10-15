

from tkinter import *
from tkinter import messagebox

class validar():
    def __init__(self):
        pass
        
    def Validarnombre(self, a):
        c = 0
        for i in a:
            if (ord(i) >=65 and ord(i)<=90) or (ord(i) >=97 and ord(i)<=122) or (ord(i)==32):
                c += 1
                if c == len(a):
                    return True
            else:
                messagebox.showerror("Error","Favor de ingresar un nombre correcto")
                return False

    def Validaredad(self,valor):
        try:
            self.a = int(valor)
            return True
        except ValueError:
            messagebox.showerror("Error", "Favor de escribir correctamente la edad")
            return False
           

    def Validarcorreo(self,correo):
        p = correo.find('@')
        if p != -1:
            nc = correo[len(correo)-4: len(correo)]
            if(nc) =='.com':
                print('Correo correcto')
                return True
            else:
                messagebox.showerror('Error', 'el correo debe terminar con  .com')
                
        else:
            messagebox.showerror('Error', 'el correo debe teber un @')
    
if __name__=="__main__":
     app= validar()
     app.Validarnombre()
     app.Validaredad()
     app.Validarcorreo()