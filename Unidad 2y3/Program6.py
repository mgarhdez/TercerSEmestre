

from tkinter import *
from tkinter import  messagebox

class Principal():
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title('Programa 1 con ventanas')
        self.ventana.geometry("400x400")
        #self.ventana.mainloop()

    def Mostrar(self):
        print('Hola mundo')
        messagebox.showinfo("Ventana","Hola mundo")


    def Disenio(self):
        self.boton1 = Button(self.ventana, text = "Aceprtar", command=self.Mostrar)
        self.boton1.pack()
        self.ventana.mainloop()


        




if __name__ == '__main__':
    app = Principal()
    app.Disenio()