# Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular y cantidad (puede tener decimales). 
# El titular será obligatorio y la cantidad es opcional. Crea sus métodos get, set y toString. Tendrá dos métodos especiales:
#   - ingresar(double cantidad): se ingresa una cantidad a la cuenta si la cantidad introducida es negativa, no se hará nada.
#   - retirar(double cantidad): se retira una cantidad a la cuenta, si restando la cantidad actual a la que nos pasan 
#     es negativa, la cantidad de la cuenta pasa a ser 0.

class Cuenta:
    def __init__(self, titular,cantidad=0):
        self.titular = titular
        self.cantidad = cantidad
    
    def getTitular(self):
        return self.titular

    def setTitular(self, new_titular):
        self.titular = new_titular

    def getCantidad(self):
        return self.cantidad

    def setCantidad(self, new_cantidad):
        self.cantidad = new_cantidad

    def __str__(self):
        return f'titular:   {self.titular}\nCantidad: {self.cantidad}€'
    
    def ingresar(self, ingreso):
        if ingreso>0:
            self.cantidad += ingreso
        
    def retirar(self, retiro):
        if retiro>0:
            self.cantidad -= retiro
            if self.cantidad<0:
                self.cantidad = 0
    
jose = Cuenta("Jose")
jose.ingresar(500.25)
jose.ingresar(100.25)
jose.retirar(300.25)
print(jose)