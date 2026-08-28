
# Hacer un progrma que lea 4 numeros y calcule 4 numeros 

a = int(input('Escribe un numero \n'))
b = int(input('Escribe un numero \n'))
c = int(input('Escribe un numero \n'))
d = int(input('Escribe un numero \n'))

promedio  = (a+b+c+d)/4
print(f'El promedio es {promedio}')

if promedio >= 7:
    print ("Si aprobo")
else:
    print("No aprobo")


