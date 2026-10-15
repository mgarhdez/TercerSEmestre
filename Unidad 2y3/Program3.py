

#Hacer un programa que lea el nombre, edad y peso de una persona, 
# el programa validarar los datos, mediante metodos recursivos
#y ademas mostrara la conversion del peso de kilos a libras
#Donde una libra son 2.5 kilogramos. El programa no termina hasta que todos los datos sean correctos

class Principal():
    def __init__(self):
        self.nombre = ''
        self.edad = ''
        self.k = ''
        self. l = ''

    def ValidarLetras(self,a):
        self.nombre = input('Escribe el nombre de una persona')
        for i in a:
            if(ord(i)>= 97 and ord(i)<=122) or ord(i)==32:
                print('El nombre es correcto')
            else:
                print('El nombre es incorrecto')
                return self.ValidarLetras(a)

    def Validarnumeros(self,a):
        self.edad = input('Escribe la edad de una persona')
        try:
            self.edad = int(a)
        except ValueError:
            print('error en la edad')
            return self.Validarnumeros(a)


if __name__ =='__main__':
    app = Principal()
    app.Validarnumeros()
    app.ValidarLetras()