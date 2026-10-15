
import time


class Principal():
    def __init__(self):
        self.numeros = [0,0,0,0,0,0,0,0,0,0,]

    def llenarArreglo(self):
        for i in range(0,10):
            self.numeros[i] = int(input(f'Escribe un numero en la posicion {i}\n'))

    def MostrarArreglo(self):
        print('Mostrar arreglo')
        for i in self.numeros:
            print(f'{i}')

    def pilas(self):
        print('PILAS')
        pos = len(self.numeros)-1
        while(pos >=0):
            print(f'El arreglo{self.numeros[pos]}')
            self.numeros[pos] = 0
            time.sleep(1)
            print(f'El arreglo actualizado: {self.numeros[pos]}')
            pos -= 1

    def Colas(self):
        print('Colas')
        for i in range(0,len(self.numeros)-1):
            print(f'El arreglo: {self.numeros[i]}')
            self.numeros[i] = 0
            time.sleep(1)
            print(f'El arreglo actualizado: {self.numeros[i]}')



if __name__=='__main__':
    clase = Principal()
    clase.llenarArreglo() 
    #clase.pilas()
    #clase.MostrarArreglo()
    clase.Colas()

























































































































































