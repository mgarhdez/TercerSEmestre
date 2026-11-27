

 #Base de datos 
from tkinter import messagebox
import sqlite3
import os

bd = 'Personas.db'
class Principal():
    def __init__(self):
        if os.path.exists(bd):
            messagebox.showinfo("Ventana","BD ya esta creada")
        else:
            con = sqlite3.connect(bd)
            cursor = con.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS usuarios(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    usuario TEXT NOT NULL,
                    password TEXT NOT NULL)
            """)

            cursor.execute("INSERT INTO usuarios(usuario,password) VALUES(?,?)",("admin", "12345"))
            con.commit()
            con.close()
            messagebox.showinfo("Ventana","EL usuario y la BD fueron creados correctamente")

    def login(self):
        u = input("Escribe el usuario\n")
        p = input("Escribe el password\n")    
        con = sqlite3.connect(bd)
        cursor = con.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE usuario=? and password=?",(u,p))
        usuarioencontrado = cursor.fetchone()
        
        cursor.close()
        if len(u)==0 or len(p)==0:
            # print("Favor de introducir un usuario")
            messagebox.showerror("Error","Favor de introducir un usuario")
            self.login()
        elif usuarioencontrado:
           # messagebox.showinfo("Ventana","El usuario y el password son correctos")
           self.menu()
        else:
            messagebox.showinfo("Ventana","El usuario o el password  no son correctos")
            self.login()

    def menu(self):
        print('1.- Agregar')
        print('2.- Eliminar')
        print('3.- Modificar')
        print('4.- Mostrar')
        print('5.- Salir')
        
        op = int(input("Escribe una opcion"))
        if op ==1:
            print("Agregar")
            self.agregar()
            self.menu()
        elif op ==2:
            print("Eliminar")
            self.eliminar() 
            self.menu()
        elif op ==3:
            print("Modificar")
            self.modificar()
            self.menu()
        elif op ==4:
            print("Mostrar")
            self.mostrar()
            self.menu()
        elif op ==5:
            print("salir") 
            return
        else:
            print('Error de opcion')
            messagebox.showinfo("Error","Error de opcion")
            self.menu()
          

    def agregar(self):
        usuario = input("Escribe un usuario\n")
        password = input("Escribe un password\n")
        con = sqlite3.connect(bd)
        cursor = con.cursor()
        cursor.execute("INSERT INTO usuarios(usuario,password) VALUES(?,?)",(usuario, password))
        con.commit()
        con.close()

    def mostrar(self):
        con = sqlite3.connect(bd)
        cursor = con.cursor()
        cursor.execute("SELECT * FROM usuarios")
        usuarioencontrado = cursor.fetchall()
        for i in usuarioencontrado:
            print(f"El usuario es: {i}")
        con.commit()
        cursor.close()
        #self.menu()
    def modificar(self):
        usuario = input("Escribe el usuario a modificar\n")
        con = sqlite3.connect(bd)
        cursor = con.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE usuario=?",(usuario,))
        usuarioencontrado = cursor.fetchone()
        if not usuarioencontrado:
            print("El usuario  a modificar no existe")
            messagebox.showinfo("error","El usuario que se desea modificar no existe")
        else:
            nusuario = input("Escribe el  nuevo usuario\n")
            npassword = input("Escribe el nuevo password\n")
            cursor.execute("UPDATE usuarios SET usuario=?, password=? WHERE id=? ",(nusuario,npassword,usuarioencontrado[0]))
            con.commit()
            con.close()
            print("EL usuario se ha modificado")
 
    def eliminar(self):
        self.mostrar()
        usuario = input("Escribe el usuario a eliminar\n")
        print(usuario)
        con = sqlite3.connect(bd)
        cursor = con.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE usuario=?",(usuario,))
        usuarioencontrado = cursor.fetchone()
        if not usuarioencontrado:
            print("El usuario a eliminar no existe")
            messagebox.showinfo("Error","El usuario a elimnar no")
            self.eliminar()
        else:
            print(usuarioencontrado[0])
            cursor.execute("DELETE FROM usuarios WHERE id=?",(usuarioencontrado[0],))
            con.commit()
            cursor.close() 
            print("Usuario Eliminado")
    
          


            
if __name__=='__main__':
    app = Principal()
    app.login()
    