

#Base de datos
import tkinter as tk
from tkinter import messagebox
from tkinter import *
import sqlite3
import os
from tkinter import ttk

bd = "Agenda.db"
class Principal():
    def __init__(self, master):
        if not os.path.exists(bd):
           self.BaseDatos()
        self.ventana = master
        self.ventana.geometry("750x200")
        self.ventana.title("login")
        Label(self.ventana, text= 'Login',
            font=("Times New Roman",18, "bold")).place(x=50,y=5)
        Label(self.ventana, text= "Escribe el usuario",
              font=("Times New Roman",12, "bold")).place(x=20,y=50)
        self.usuario = Entry(self.ventana)
        self.usuario.place(x=170,y=53)
        Label(self.ventana, text= "Escribe el password",
              font=("Times New Roman",12, "bold")).place(x=20,y=90)
        self.password = Entry(self.ventana)
        self.password.place(x=170,y=93)
        Button(self.ventana, text='Aceptar', width=10, command= self.login).place(x=50 ,y=130 )
        Button(self.ventana, text='Salir', width= 10, command= self.cerrar).place(x=150 ,y=130 )
        self.ventana.mainloop()


    def BaseDatos(self):
        con = sqlite3.connect(bd)
        cursor = con.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS usuarios(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                usuario TEXT NOT NULL,
                tipo Text NOT NULL,
                password TEXT NOT NULL)
        """)
        cursor.execute("""CREATE TABLE IF NOT EXISTS datos(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nombre TEXT NOT NULL,
                        telefono Text NOT NULL,
                        correo TEXT NOT NULL,
                        id_usuario INTEGER,
                        FOREIGN KEY (id_usuario) REFERENCES usuarios(id)
                        )
        """)

        cursor.execute("INSERT INTO usuarios(usuario,tipo,password) VALUES(?,?,?)",("admin","administrador","12345"))
        con.commit()
        con.close()

    def cerrar(self):
        self.ventana.destroy()

    def login(self):
        us = self.usuario.get()
        pas = self.password.get()
        if len(us) ==0 or len(pas) ==0:
            messagebox.showerror("Error", "Faltan datos")
        else:
            con = sqlite3.connect(bd)
            cursor = con.cursor()
            cursor.execute("SELECT * FROM usuarios WHERE usuario=? and password=?",(us, pas))
            res = cursor.fetchone()
            if not res:
                messagebox.showerror("ERROR","El usuario no existe")
                self.usuario.delete(0,END)
                self.password.delete(0,END)
            else:
               # messagebox.showinfo("Ventana","si existe")
                self.ventana.withdraw()
                otra = Toplevel(self.ventana)
                Secundaria(otra,self.ventana)
                self.usuario.delete(0,END)
                self.password.delete(0,END)
                



class Secundaria():
    def __init__(self,master,ventana):
        self.ventana = ventana
        self.ventana2 = master
        self.ventana2.title("Ventana 2")
        self.ventana2.geometry("750x500")
        self.menu = tk.Menu(self.ventana2)
        self.ventana2.config(menu = self.menu)
        self.archivo = tk.Menu(self.menu, tearoff=0)
        self.archivo.add_command(label="Salir", command=self.salir)
        self.menu.add_cascade(label="Archivo", menu=self.archivo)
        #Diseño de la ventana
        Label(self.ventana2, text= 'Mostrar datos de los usuarios',
            font=("Times New Roman",18, "bold")).place(x=50,y=5)
        Label(self.ventana2, text= "Escribe el usuario",
                font=("Times New Roman",12, "bold")).place(x=20,y=50)
        self.usuario = Entry(self.ventana2)
        self.usuario.place(x=170,y=53)
        Label(self.ventana2, text= "Escribe el password",
                font=("Times New Roman",12, "bold")).place(x=20,y=90)
        self.password = Entry(self.ventana2)
        self.password.place(x=170,y=93)
        Label(self.ventana2, text= "Elije el tipo",
                font=("Times New Roman",12, "bold")).place(x=20,y=130)
        self.tipo = ttk.Combobox(self.ventana2, values=["Administrador","Jefe de Area","Supervisor","Empleado"])
        self.tipo.place(x=130, y=133)
        Label(self.ventana2, text= "Escribe el nombre",
                font=("Times New Roman",12, "bold")).place(x=300,y=50)
        self.nombre = Entry(self.ventana2)
        self.nombre.place(x=430,y=53)
        Label(self.ventana2, text= "Escribe el telefono",
                font=("Times New Roman",12, "bold")).place(x=300,y=90)
        self.telefono = Entry(self.ventana2)
        self.telefono.place(x=430,y=93)
        Label(self.ventana2, text= "Escribe el correo",
                font=("Times New Roman",12, "bold")).place(x=300,y=130)
        self.correo = Entry(self.ventana2)
        self.correo.place(x=430,y=133)
        Button(self.ventana2, text='Agregar', width=10,command=self.Agregar).place(x=50 ,y=180 )
        Button(self.ventana2, text='Eliminar', width=10,command = self.Eliminar).place(x=150 ,y=180 )
        Button(self.ventana2, text='Modificar', width=10,command=self.Modificar).place(x=250 ,y=180 )
        columnas = ["ID","USUARIO","TIPO","PASSWORD","ID DATOS","NOMBRE","TELEFONO","CORREO"]
        
        self.tabla = ttk.Treeview(self.ventana2,columns= columnas, show="headings")
        self.tabla.place(x=30,y=210, width=700, height=200)
        for col in columnas:
            self.tabla.heading(col, text= col)
            self.tabla.column(col,anchor="center", width=41)
        scroll = ttk.Scrollbar(self.ventana2,orient="horizontal",command=self.tabla.xview)
        self.tabla.config(xscroll =scroll.set)
        scroll.place(x=30 ,y=370, height=710, width=690)
        self.tabla.bind("<<TreeviewSelect>>",self.elegirFila)
        self.Mostrar()
        self.fila = 0
        self.id = 0
        self.id_usuario = 0
        self.id_datos = 0
        self.agregarPersona = False
        self.ventana2.mainloop()



    def Mostrar(self):
        print("mostrar")
        con = sqlite3.connect(bd)
        cursor = con.cursor()
        cursor.execute("""
            SELECT usuarios.id,
                usuarios.usuario,
                usuarios.tipo,
                usuarios.password,
                datos.id,
                datos.nombre,
                datos.telefono,
                datos.correo,
                datos.id_usuario
            FROM usuarios
            INNER JOIN datos
            ON usuarios.id = datos.id_usuario
        """)
        elementos = cursor.fetchall()
        if not elementos:
            messagebox.showerror("error","No hay elementos")
            return
        for fila in elementos:
            print(fila)
            self.tabla.insert("",END, values=fila)
        con.close()
    # def Mostrar(self):
    #     con = sqlite3.connect(bd)
    #     cursor = con.cursor()
    #     cursor.execute("SELECT * FROM usuarios")
    #     res = cursor.fetchall()
    #     if not res:
    #         messagebox.showerror("Error","La tabla usuarios esta vacia")
    #     else:
    #         for fila in res:
    #             self.tabla.insert("",END, values=fila)
    #         con.close()

    def elegirFila(self,event):
        self.borrarCajas()
        try:
            self.fila = self.tabla.selection()[0]
        except:
            return
        print(f'La fila seleccionada es:{self.fila}')
        datosfila = self.tabla.item(self.fila, "values")
        self.id = datosfila[0]
        self.usuario.insert(0,datosfila[1])
        self.password.insert(0,datosfila[3])
        self.id_datos = datosfila[4]
        self.nombre.insert(0,datosfila[5])
        self.telefono.insert(0,datosfila[6])
        self.correo.insert(0,datosfila[7])
        self.id_usuario = datosfila[8]
        self.agregarPersona = True
       
         
       # print(f'usuario: {datosfila[1]}')

    def borrarCajas(self):
        self.usuario.delete(0,END)
        self.password.delete(0,END)
        self.tipo.delete(0,END)
        self.nombre.delete(0,END)
        self.telefono.delete(0,END)
        self.correo.delete(0,END)
        self.tipo.delete(0,END)

    def Modificar(self):
        if self.fila ==0:
            messagebox.showerror("ERROR","Primero elige un usuario")
        else:
            u = self.usuario.get()
            p = self.password.get()
            t = self.tipo.get()
            n = self.nombre.get()
            tl = self.telefono.get()
            c = self.correo.get()
            if len(u)==0 or len(p)==0 or len(t)==0 or len(n)==0 or len(tl)==0 or len(c)==0:
                messagebox.showerror("Error","Faltan datos")
            else:
                con = sqlite3.connect(bd)
                cursor = con.cursor()
                cursor.execute("UPDATE usuarios SET usuario=?, tipo=?, password=? WHERE id=?",(u,t,p,self.id))
                cursor.execute("UPDATE datos SET nombre=?, telefono=?, correo=? WHERE id=?",(n,tl,c,self.id_usuario))
                con.commit()
                con.close()
                messagebox.showinfo("Ventana","Los datos se actualizaron")
                self.borrarCajas()
                self.actualizar()
                self.fila == 0
                self.agregarPersona == False



    def Eliminar(self):
        if self.fila ==0:
            messagebox.showerror("ERROR","Primero elige el usuario")
        else:
            con = sqlite3.connect(bd)
            cursor = con.cursor() 
            cursor.execute("DELETE FROM usuarios WHERE id=?"(self.id,))
            cursor.execute("DELETE FROM datos WHERE id=?"(self.id_usuario,))
            con.commit()
            con.close()
            messagebox.showinfo("ventana","El usuario se a eliminado")
            self.actualizar()
            self.fila = 0
            self.Mostrar()
            self.agregarPersona == False

    def Agregar(self):
        if self.agregarPersona == False:
            u = self.usuario.get()
            p = self.password.get()
            t = self.tipo.get()
            n = self.nombre.get()
            tl = self.telefono.get()
            c = self.correo.get()
            if len(u)==0 or len(p)==0 or len(t)==0 or len(n)==0 or len(tl)==0 or len(c)==0:
                messagebox.showerror("Error","Faltan datos")
            else:
                con = sqlite3.connect(bd)
                cursor = con.cursor() 
                cursor.execute("INSERT INTO usuarios(usuario,tipo,password) VALUES(?,?,?)",(u,t,p))
                id_usuario = cursor.lastrowid
                cursor.execute("INSERT INTO datos(nombre,telefono,correo,id_usuario) VALUES(?,?,?,?)",(n,tl,c,id_usuario))
                con.commit()
                con.close() 
                messagebox.showinfo("Ventanta","El usuario se agrego correctamente")
                self.borrarCajas()
                self.actualizar()
               
        else:
            messagebox.showerror("ERROR","Estas modificando o eliminando")
            
            

    def actualizar(self):
        for iten in self.tabla.get_children():
            self.tabla.delete(iten)
            self.borrarCajas()
           
            
            
    def salir(self):
        self.ventana2.destroy()
        self.ventana.destroy()



if __name__=='__main__':
    master = Tk()
    app = Principal(master)
    app.login()


    