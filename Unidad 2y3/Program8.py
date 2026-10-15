
from tkinter import *
from tkinter import messagebox

#place
class Principal():
    def __init__(self):
        self.ventana = Tk()
        self.ventana.geometry("400x200")
        self.ventana.title("Practica 8")
        self.ventana.configure(bg="#D10404")
        self.lista = []
      #  self.ventana.mainloop()

    def Calcular(self):
        n1 = self.n1.get()
        n2 = self.n2.get()
        if(len(n1)==0 or len(n2)==0):
           messagebox.showerror("error", "Faltan datos")
        else:
           self.lista.append(n1 +" _ "+n2)
           print(self.lista)
           self.mensaje.config(text=self.lista)
           self.n1.delete(0,END)
           self.n2.delete(0,END)
           

    def Cerrar(self):
        self.ventana.destroy()

    def Disenio(self):
        Label(self.ventana, 
            text= "Practica 8",
            font = ("Arial",18, "bold"),
            fg="#C0C0C0",
            bg="#D9592E").place(x=100, y=10)# x es columna y y es fila
        Label(self.ventana, 
            text= "Escribe un numero",
            fg="#C0C0C0",
            bg="#D9592E").place(x=10, y=50)
        self.n1 = Entry(self.ventana,
            fg="#C0C0C0",
            bg="#D9592E")
        self.n1.place(x=125, y=50)
        Label(self.ventana, 
            text= "Escribe otro numero",
            fg="#C0C0C0",
            bg="#D9592E").place(x=10, y=80)
        self.n2 = Entry(self.ventana,
            fg="#C0C0C0",
            bg="#D9592E")
        self.n2.place(x=125, y=80) 
        Button(self.ventana, 
            text= "Calcular", 
            command=self.Calcular,
            fg="#C0C0C0",
            bg="#D9592E",
            widt=10).place(x=150, y=120)
        Button(self.ventana, 
            text= "Cerrar", 
            command=self.Cerrar,
            fg="#C0C0C0",
            bg="#D9592E", 
            width=10).place(x=220, y=120)
        self.mensaje = Label(self.ventana, 
            text= "",
            font = ("Arial",18, "bold"),
            fg="#C0C0C0",
            bg="#D9592E")# x es columna y y es fila
        self.mensaje.place(x=100, y=150)
        self.ventana.mainloop()









if __name__ =='__main__':
    app = Principal()
    app.Disenio()
    