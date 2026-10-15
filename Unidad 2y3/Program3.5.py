


class Principal():
    def __init__(self):
        self.nombre =""
        self.edad = 0
        self.estatura = 0.0
    

        # self.Leer()

    def ValidarNombre(self, a):
        c = 0
        for i in a:
            if (ord(i) >=65 and ord(i)<=90) or (ord(i) >=97 and ord(i)<=122) or (ord(i)==32):
                c += 1
        if c == len(a):
            return True
        else:
            return False


    def Leer(self):
        self.nombre = input('Escribe un nombre \n')
        if self.ValidarNombre(self.nombre):
            print('Nombre correcto')
            self.PedirEdad()
        else:
            print('Errror en el nombre')
            return self.Leer()
        
    def ValidarEdad(self,a):
        try:
            self.edad = int(a)
            return True
        except ValueError:
            return False
        


    def PedirEdad(self):
        self.edad = input('Escribe una edad\n')
        if self.ValidarEdad(self.edad):
            print('Edad correcta')
            self.PedirEstatura()
        else:
            print('error en la edad')
            return self.PedirEdad()

    def ValidarEstatura(self,a):
        try:
            self.estatura = float(a)
            return True
        except ValueError:
            return False

    def PedirEstatura(self):
        self.estatura = input('escribe una estatura\n')
        if self.ValidarEstatura(self.estatura):
            print('Estatura correcta')
        else:
            print('error en la estatura')
            return self.PedirEstatura()
        
    

if __name__=='__main__':
    app = Principal()
    app.Leer()
    
