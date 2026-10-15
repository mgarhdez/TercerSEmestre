
#HAcer un programa que lea un numero que pueda ser positivo o negrativo, debe de aver 2 listas, 
#1 para mostrar numeros negativos y ptra para mostrar numeros positivos. 
#Dependiendo del nuemro introducido se mostrara en su lista correspondiente
#abajo de cada lista aparecera un boton para vaciarlas de la siguiente manera:
#Los numeros negativos se variaran en forma de pila y los numeros positivos se vaciaran en forma de cola 

from tkinter import *
from tkinter import messagebox
import time 

class Principal():
    def __init__(self):
        self.ventana = Tk()
        self.ventana.geometry("400x250")
        self.ventana.title("Practica 12")
        self.n = 0
        self.num = ""

    def Validar(self,a):
        nn= 0
        try:
            nn = int(a)
            return True
        except ValueError:
            messagebox.showerror("Error", "No es un numero")
            self.numero.delete(0,END)
            return False

    def Agregar(self):
        print(self.lista1.size())
        print(self.lista2.size())
        self.num = self.numero.get()
        if len(self.num) == 0:
            messagebox.showerror("Error", "Escribe un numero")
        else:
            if self.Validar(self.num):
               self.n = int(self.num)
               if self.n <0:
                   self.lista2.insert(self.lista2.size()+1,self.n)
                   self.numero.delete(0,END)
               elif self.n>0:
                   self.lista1.insert(self.lista1.size()+1,self.n)
                   self.numero.delete(0,END)
               

    def Vaciar1(self):
        print(self.lista2.get(self.lista2.size()-1))
        self.lista2.delete(self.lista2.size()-1)
        if self.lista2.size()< 0:
            return 
        
    def Vaciar2(self):      
       while(True):
            print(self.lista1.get(0))
            self.lista1.delete(0)
            self.update()
            time.sleep(1)
            if self.lista1.size()< 0:
                return 
    
    def Disenio(self): 
        Label(self.ventana, text= 'Programa 11 Listas ',
            font=("Times New Roman",18, "bold")).place(x=150,y=5) 
        Label(self.ventana, text= "Escribe un numero").place(x=20,y=50)
        self.numero = Entry(self.ventana)
        self.numero.place(x=20,y=70)
        self.lista1 = Listbox(self.ventana, height=9, width=13, activestyle="dotbox")
        self.lista1.place(x=300, y=50)
        self.lista2= Listbox(self.ventana, height=9, width= 13, activestyle="dotbox")
        self.lista2.place(x=200 , y= 50)
        Button(self.ventana, text='Agregar', command = self.Agregar).place(x=20 ,y=100 )
        Button(self.ventana, text='Vaciar Lista como pila', command = self.Vaciar1).place(x=145 ,y=220 )
        Button(self.ventana, text='Vaciar lista como cola', command = self.Vaciar2).place(x=270 ,y=220 )
        self.ventana.mainloop()




if __name__=='__main__':
    app = Principal()
    app.Disenio()
