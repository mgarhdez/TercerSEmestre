


class Validaciones():
   
    def ValidarLetras(self, a):
        c = 0
        c2 = 0
        for i in a:
            if(ord(i)>= 97 and ord(i)<=122) or ord(i)==32:
                c += 1
            if ord(i) >= 65 and ord(i) <= 90:
                c2 += 1
        if c + c2 == len(a):
            return True
        else:
            return False
        
    def  validarNumeros(self,a):
        try:
            a = int(a)
            return True
        except ValueError:
            print('No son numeros enteros')
        return False

    def ValidarNumerosDecimales(self,a ):
        i = a.find ('.')
        if i == -1:
            return False
        else:
            try:
                v = float(a)
                return True 
            except ValueError:
                return False


    def ValidarCaducidad(self,a):
        fecha = 0
        i = a.find('/')
        if i == -1:
            print('fecha incorrecta')
            return False
        else:
            if i ==0:
                return False
            else:
                if i == len(a)-1:
                    return False
                else:
                    na = a.replace('/','')
                    try:      
                        fecha = int(na)
                        if fecha > 0:
                         print('fecha correcta')
                         return True
                        else:
                            return False
                    except ValueError:
                        print('fecha incorrecta')
                        return False

    def ValidarCorreoElectronico(self,correo):
        p = correo.find('@')
        if p != -1:
            nc = correo[len(correo)-4: len(correo)]
            if(nc) =='.com'or (nc) == '.mx'or (nc) =='.edu':
                print('Correo correcto')
                return True
            else:
                print('Error el correo debe tener .com o .mx o ,edu')
                
        else:
            print('Error el correo debe teber un @')


    def ValidarNumeroTelefonico(self,telefono):
        if len(telefono) != 13:
            print('Error al escribir el telefono, tienen que ser 13 digitos')
        else:
            try:
                t = int(telefono)
                print('El numero telefonico es correcto')
                self.val = True
                return self.val
            except ValueError:
                print('Deben de ser solo numeros en el telefono')
                self.val = False
                return self.val
            



























































    
    

