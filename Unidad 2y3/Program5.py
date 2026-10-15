
#Tarea 
# De los temas de la unidad 3 investigar los conceptos de pilas colas y listas


import time


class Principal():
    def __init__(self):
        self.numeros = []

    def llenarLIsta(self):
        while(True):
            self.numeros.append(int(input(f'Escribe un numero \n')))
            print(f'La lista tiene { len(self.numeros )} de elementos\n')
            res = input('Deseas otro numero s/n\n')
            if res == 'n' or res == 'N':
                break

    def MostrarLista(self):
        print('Mostrar arreglo\n')
        print(self.numeros)

    


if __name__=='__main__':
    clase = Principal()
    clase.llenarLIsta()
    clase.MostrarLista()
   
