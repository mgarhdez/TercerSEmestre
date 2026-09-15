
import sys


def validarNumerosEnteros(x):
    a = 0
    try:
        a = int(x)
        return True
    except ValueError:
        print('No son numeros enteros')
        return False
    

def valiidarNumerosDecimales(x):

    a = 0.0
    try:
         a = float(x)
         return True
    except ValueError:
        print('No son numeros decimales')
    return False
        

def validarLetras(x):
    if x.isupper():
        print('son mayusculas')
        return True
    elif x.islower():
        print('Son minusculas')
        return True
    else:
        return False
        



def inicio():
    a = input('escribe un dato')
    if validarLetras(a):
        print('son letras')
    elif validarNumerosEnteros(a):
        print('sonn numeros enteros ')
    elif valiidarNumerosDecimales(a):
        print ('son numeros con decimales')
    else:
        print('son tipos de datos distintos a los anteriores')
    sys.exit()


if __name__ =='__main__':
    inicio()