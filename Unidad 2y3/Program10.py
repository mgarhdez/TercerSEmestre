
# Hacer un programa que mediante ventanas pida un nombre, solo un nombre sin apellidos,
# si el nommbre comienza con la primera letra en mayuscula, se agregagra a una lista
# para mostrarlo en una etiqueta o label, si el nombre contiene caracteres incorrectos o no comienza 
# con mayuscula , Mostrara un mensjae de error y no se agregara a la lista 



from tkinter import *
from tkinter import messagebox


class Principal():
    def __init__(self):
        self.ventana = Tk()
        self.ventana.geometry("400x200")
        self.ventana.title("Practica 10")
        self.nombre =""
        self.lista=[]

    def ValidarDatos(self):
        if self.nombre.isalpha():
            print('Nombre correcto')
            if self.nombre[0]==self.nombre[0].upper():
                return True
            else:
              
                return False
        
        else:
            return False
       
        
   

    def MostrarDatos(self):
        self.nombre = self.n1.get()
        if self.ValidarDatos():
            self.lista.append(self.nombre)
            self.mensaje.config(text=self.lista)
        else:
            messagebox.showerror("Errorr","Nombre no Valido")
           



    def Disenio(self):
        Label(self.ventana,  text="Programa 10",
        font=("Times New Roman",18, "bold")).grid(row=1, column=1, pady=2)
        Label(self.ventana, text="Nombre").grid(row=2,column=2,pady=10)
        self.n1 = Entry(self.ventana, bg="#D7D7D8", fg="#070707")
        self.n1.grid(row=2,column=3,pady=10)
        Button(self.ventana, text="Mostrar", command=self.MostrarDatos).grid(row=5,column=1)
        self.mensaje =Label(self.ventana,  text="",
            font=("Times New Roman",18, "bold"))
        self.mensaje.grid(row = 7, column = 1, pady=2)
        self.ventana.mainloop()









if __name__=='__main__':
    app = Principal()
    app.Disenio()