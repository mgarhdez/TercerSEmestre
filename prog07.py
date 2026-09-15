#tarea
# investigar los metodos de la clase string para python 
# como obtener el valor ascii de un caracter en python 

#Hacer un programa que lea un numero correspondiente de 1 y 9, a continuacion realizara una pregunta indicando
#si desea introducir otro numero si la respuesta es si realizara nuevamente el proceso de lectura de datos,
#si la respuesta es no el programa mostrar la suma, promedio y cantidad de numeros introducidos
#ademas de los numeros que se introdujeron 

c = 0
p = "s"
suma = 0
su = ","
while(p =="s"):
    a = int(input('Escribe un numero \n' ))#Verificar que el numero sea entre 1 y 9 
    if a >=1 and a <=9:
        c += 1
        suma += a 
        su += str(a)
        su += ","
        p = input('Deseas introducir otro numero s/n \n')
        if p == "s" or "S":
            print("Se introducira otro numero")
        else:
            break
    else:
        print("El numero no esta entre 1 y 9 \n vuelve a intentarlo")

print(f'La suma de los numeros son { suma} y el promedio es { suma/c} y la cantidad de los numeros son { c}\n y los numeros involucrados son{su}')





