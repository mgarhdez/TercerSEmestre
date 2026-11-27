

from tkinter import *
from tkinter import messagebox
import random

class Principal():
    def __init__(self,):
        self.ventana = Tk()
        self.ventana.geometry("400x600")
        self.ventana.title("Preexamen")
        self.c = 0
        self.n1 = random.randint(1,20)  
        self.n2 = random.randint(20,50)
        self.n3 = random.randint(50,100)
    def generar(self):


        

        self.c +=1
        if self.c==1 :
            self.Lista1.insert(self.Lista1.size()+1,self.n1)
            self.Lista2.insert(self.Lista2.size()+1,self.n2) 
            self.Lista3.insert(self.Lista3.size()+1,self.n3)
        elif self.c==2: 
            self.Lista1.insert(self.Lista1.size()+1,self.n1)
            self.Lista2.insert(self.Lista2.size()+1,self.n2) 
            self.Lista3.insert(self.Lista3.size()+1,self.n3)
        elif self.c==3:
            self.Lista1.insert(self.Lista1.size()+1,self.n1)
            self.Lista2.insert(self.Lista2.size()+1,self.n2) 
            self.Lista3.insert(self.Lista3.size()+1,self.n3)
        else:
            messagebox.showerror("Error","Se paso con el maximo permitido")
        

    def Disenio(self):
        
        self.Lista1 = Listbox(self.ventana,height=10,width=40)
        self.Lista1.place(x=20, y=20)
        self.Lista1.insert(END,f'{'Nombre'}')

        self.Lista2 =Listbox(self.ventana, height=10,width=40)
        self.Lista2.place(x=20, y=190)
        self.Lista2.insert(END,f'{'Edad'}')

        self.Lista3 =Listbox(self.ventana, height=10,width=40)
        self.Lista3.place(x=20, y=300)
        self.Lista3.insert(END,f'{'Telefono'}')
        Button(self.ventana, text="generar", command=self.generar).place(x=300 ,y=190)
        self.ventana.mainloop()

if __name__=="__main__":
    app = Principal()
    app.Disenio()