

from validaciones import Validaciones


class Programa():
   def  __init__(self):
        self.val = Validaciones()
        

   
   def pedirDatos(self):
       self.nombre = input('Escribe el nombre\n')
       self.edad = input('Escribe la edad\n')
       self.estatura = input('Escribe la estatura\n')
       if self.val.ValidarLetras(self.nombre):
            print('El nombre es correcto...')
       else:
           print('error con el nombre')
       if self.val.validarNumeros(self.edad):
            print ('La edad es correcta...')
       else:
            print('error con la edad')
       if self.val.ValidarNumerosDecimales(self.estatura):
            print('la estatura es correcta...')
       else:
           print('error en la estatura')
        

        
        
       
    





if __name__ == '__main__':
    while(True):
        app = Programa()
        app.pedirDatos()
        res = input("Deseas intentarlo otra vez  s/n")
        if res == 'N' or res == 'n':
            break

   
