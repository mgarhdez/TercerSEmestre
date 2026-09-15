

# HAcer un progrma que te pida 10 veces una letra y al final mostrara todo junto en un solo renglon 


suma  = 0
for i in range(1,11):
    a = int(input('Escribe una letra \n'))
    suma += a
print(f'todas los numeros seleccionados son {suma}')

a = ""

for x in range(1,11):
    letra = input('escribe una letra ')
    a += letra 

print(f'las letras son {a} y tiene una longuitud de {len(a)}')



