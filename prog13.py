
# Hacer un programa que lea nombre, apellido materno y apellido paterno dentro de una variable, 
# A  continuacion pedira correo electronico y telefono de la persona.
# Estos datos tienen quer estar previamente validados de lo contrario se volveran a pedir.
# Las validaciones son las siguientes 
# 1.- solo puede tener un nombre y sus apellidos 
# 2.- Cada elemento del nombre debe comenzar con mayuscula
# 3.- El correo electronico permite cualquier tipo de caracter pero obligatoriamente debe llevar una sola @ y terminar con .com
# 4.- El telefono son unicamnete numeros y obligatoriamente 10 digitos 

from validaciones import Validaciones




class programa():
    def __init__(self):
        self.val = Validaciones()
        self.nombre = ''
        self.correo = ''
        self.telefono = 0

    def pedirDatos(self):
        while(True):
            self.nombre = input('Escribe el nombre completo\n')
            b = self.nombre.split(' ')
            if(len(b) == 3):
                print('estructura correcta')
                ns =b[0]
                nc = b[1]
                ne = b[2]
                if ns[0] == ns[0].upper() and nc[0] == nc[0].upper() and ne[0]==ne[0].upper():
                    if self.val.ValidarLetras(self.nombre):
                        print(f'el nombre fue:{self.nombre}')     
                        break              
                    else:
                        print('El nombre o los apellidos son invalidos  \n favor de volver a ingresarlo')
                       
                else:
                    print('No es mayuscula')
                    
                    
            else:
                print('Escribe solo un nombre con tus dos apellidos')
               


        while(True):
            self.correo = input('Escribe un correo electronico\n')
            if self.val.ValidarCorreoElectronico(self.correo) :
                break
            else:
                print(' favor de volver a intentar')

        while(True):
            self.telefono = input('Escribe un numero telefonico\n')
            if self.val.ValidarNumeroTelefonico(self.telefono):
                break
            else:
                print ('Favor de volver a intentar')
            break
                

if __name__ == '__main__':
    app = programa()
    app.pedirDatos()
    print(f'El nombre ingresado es:{app.nombre}\n Su correo electronico es: {app.correo} El telefono es: {app.telefono}')
