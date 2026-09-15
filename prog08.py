
# a = "Hola"
# for i in a:
#     print(ord(i)) # para mostrar el ascii del caracter

import sys  # importamos la libreria para instrucciones del sistema

def ValidarDatos(a):
    c = 0
    c2 = 0
    for i in a:
        if ord(i) >= 97 and ord(i)<=122:
            c += 1
        if ord(i) >= 48  and ord(i)<=57:
            c2 += 1
    if c == len(a):
            return True
    elif c2 == len(a):
            return False
    else:
            print('Existen letras y numeros mezclados ')
            sys.exit() #Termina eñ progrma sin importar si existen mas lineas de codigo
            

def pedirDatos():
    pass
    a = input('Escribe un dato ')
    if ValidarDatos(a):
        print('Son puras letras ')
    else:
        print('Son numeros ')
        
 
if __name__=='__main__':
    pedirDatos()
