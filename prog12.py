


# Hacer un programa que lea nombre de un producto, fecha de caducidad que solo contenga mes y año y su respectivo precio.
# Una vez validados los datos el programa mostrara un mensaje indicando si desean otro producto,
# si es asi vulve hacer el mismo proceso  de lo contrario mostrara el total de los precios, la cantidad de productos y 
# el total con iva

from validaciones import Validaciones



class programa():
    
    def __init__(self):
        self.val = Validaciones()
        self.nombre = ''
        self.precio = 0
        self.caducidad = ''
        self.contador = 0
        self.suma = 0
        
        
    def pedirDatos(self):
    
            
        while(True):
            self.nombre = input('Escribe el nombre del producto\n')
            if self.val.ValidarLetras(self.nombre):
                print(f'el producto ingresado fue:{self.nombre}')
                self.contador+= 1
                
                break
                
            else:
                print('El nombre del producto ingresado es erroneo  \n favor de volver a ingresarlo')
                
        while(True):      
            self.precio = input('Escribe el precio del producto\n')
            if self.val.validarNumeros(self.precio):
                print(f'el  precio del producto es:{self.precio}')
                self.suma += int(self.precio)
                print(f'La suma de precio del producto es:{self.suma}')
                break
            else:
                print('El precio ingresado  del producto  es erroneo')

        while(True):
            self.caducidad = input('Escribe la decha de caducidad\n')
            if self.val.ValidarCaducidad(self.caducidad):
                print(f'la fecha de caducidad es:{self.caducidad}')                    
                break
            else:
                print('El fecha de caducidad ingresada es erroneo')
               
            

if __name__ == '__main__':
    app = programa()
    while(True):
        app.pedirDatos()
        res = input('Deseas escribir otro produccto s/n \n')
        if res == 'n' or res =='N':
            iva= app.suma * 1.16
            total_iva= iva + app.suma
            print(f'Los productos imgresados son: \n{app.contador}\n la suma de los precios ingresados fueron:\n {app.suma} \nel total con iva es:{total_iva}')   
            break
         


