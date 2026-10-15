


from tkinter import *
from tkinter import  messagebox

#pack
class Principal():
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title('Programa 1 con ventanas')
        self.ventana.geometry("400x400")
        self.num1 = ""
        self.num2 = ""
        self.a = 0
        self.b = 0
        self.suma = 0
        #self.ventana.mainloop()

    def ValidarNumeros(self,valor):
        try:
            self.a = int(valor)
            return True
        except ValueError:
            return False

    def Mostrar(self):
        # print('Hola mundo')
        # messagebox.showinfo("Ventana","Hola mundo")
        self.num1 = self.n1.get()
        self.num2 = self.n2.get()
        if self.ValidarNumeros(self.num1) and self.ValidarNumeros(self.num2):
            self.a = int(self.num1)
            self.b = int(self.num2)
            self.suma = self.a + self.b
            self.n1.delete(0,END)
            self.n2.delete(0,END)
            messagebox.showinfo('Suma',f'El resultado de la suma es: {self.suma}')
        else :
            messagebox.showerror("Error", "No son numeros")
            self.n1.delete(0,END)
            self.n2.delete(0,END)

    def Disenio(self):
        Label(self.ventana,text="Escribe un numero").pack()
        self.n1 = Entry(self.ventana)
        self.n1.pack()
        Label(self.ventana,text="Escribe un numero").pack()
        self.n2 = Entry(self.ventana)
        self.n2.pack()
        self.boton1 = Button(self.ventana, text = "Suma", command=self.Mostrar)
        self.boton1.pack()
        self.ventana.mainloop()

                                                                                
if __name__ == '__main__':
    app = Principal()
    app.Disenio()