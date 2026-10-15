
from tkinter import *
from tkinter import messagebox


#grid 
class Principal():
    def __init__(self):
        self.ventana = Tk()
        self.ventana.geometry("400x200")
        self.ventana.title("Practica 9")
        self.lista=[]
        self.n1 = StringVar
        self.n2 = StringVar
        self.x1=""
        self.x2=""
       

    def ValidarNumeros(self,v):
        a=0
        try:
            a=int(v)
            return True
        except ValueError:
            messagebox.showerror("Error", "No es un numero")
            return False
    def EncomtrarNumeros(self,w):
        #w =int(self.x1)+1
        print(int(w))
        if int(w)>=int(self.x2)-1:
            print('Fin')
            return 
        else:
            self.lista.append(int(w)+1)
            return self.EncomtrarNumeros(int(w)+1)


    def MostrarNumeros(self):
        n1 = self.n1.get()
        n2 = self.n2.get()
        if(self.ValidarNumeros(n1)or self.ValidarNumeros(n2)):
            if int(n1)< int(n2):
                self.x1=n1
                self.x2=n2
                self.EncomtrarNumeros(self.x1)
            #     for i in range(int(n1), int(n2)):
            #         self.lista.append(i)
                self.mensaje.config(text=self.lista)
            else:
                messagebox.showerror("Errorr","Se ocupa que el segundo numero sea mayor al primero")
                self.n1.delete(0,END)
                self.n2.delete(0,END)


    def disenio(self):
        Label(self.ventana,  text="Programa 9",
            font=("Times New Roman",18, "bold")).grid(row=1, column=1, pady=2)
        Label(self.ventana, text="Numero 1").grid(row=2,column=2,pady=10)
        self.n1 = Entry(self.ventana, bg="#D7D7D8", fg="#070707")
        self.n1.grid(row=2,column=3,pady=10)
        Label(self.ventana, text="Numero 2").grid(row=3,column=2)
        self.n2 = Entry(self.ventana)
        self.n2.grid(row=3,column=3)
        Button(self.ventana, text="Mostrar", command=self.MostrarNumeros).grid(row=5,column=1)
        self.mensaje =Label(self.ventana,  text="",
            font=("Times New Roman",18, "bold"))
        self.mensaje.grid(row = 7, column = 1, pady=2)
        self.ventana.mainloop()





if __name__=='__main__':
    app=Principal()
    app.disenio()