
class Principal():
    def __init__(self):
        self.dato = 0
        self.con = 0
        self.a = "2"
        self.Leer(self.a)
        

    def Leer(self,a):
        self.dato = int(a)**2
        print(self.dato)
        self.con += 1
        if self.con >=10:
            print('Se ejecuto 10 veces el programa')
        else:
            print(f'El valos de la variable{(int(a)+1)}')
            return self.Leer(int(a)+1)





if __name__ == '__main__':
    app = Principal()