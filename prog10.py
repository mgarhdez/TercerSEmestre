
# Tarea
# Hacer un programa que pida una cantidad en pesos(numeros con decimales)el programa validara que sea un numero correcto 
# y si el dato es correcto calculara y mostrara su equivalente en dolares y euros. si el numero es incorrecto 
# se volvera a pedir.
# El programa no termina hasta que muestre en pantalla los resultados solicitados

import sys


def validarNumeros(a):
    i = a.find('.')
    if i == -1:
        return False
    else :
        #print ('Si tiene punto')
        try:
            v = float(a)
            return True
        except ValueError:
            return False

def inicio():
    al = 0.0
    cd = 0.0
    ce = 0.0
    while(True):
        a = input('Escribe una cantidad en pesos (con decimales)\n')
        if validarNumeros(a):
            al = float(a)
            cd = al / 16.95
            print(f'La conversion a dolares es {cd}')
            ce = al / 19.67
            print (f'La conversion a euros es {ce}')
            break 
            #sys.exit
        else:
            print('Error valor erroneo \n Favor de volver a ingresar un numero')


if __name__=='__main__' :
    inicio()


# def validarDecimales(x):
#     a = 0.0
#     try:
#         a = float(x)
#         return True
#     except ValueError:
#         return False




# def inicio():
#     while True:
#         a = input('Ingresa una cantidad en pesos (con decimal): ')
#         if validarDecimales(a):
#             pesos = float(a)
            
#             # Tasas de conversión (ejemplo fijo)
#             dolar = 0.056   # 1 peso ≈ 0.056 dólares
#             euro = 0.052    # 1 peso ≈ 0.052 euros
            
#             # Calcular equivalentes
#             dolares = pesos * dolar
#             euros = pesos * euro
            
#             # Mostrar resultados
#             print(f"\nEquivalente en dólares: {dolares}")
#             print(f"Equivalente en euros: {euros:}")
            
#             # Terminar el programa
#             sys.exit()
#         else:
#             print("Por favor, ingresa un número válido.\n")

# if __name__ == '__main__':
#     inicio()
     