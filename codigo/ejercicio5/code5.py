class Vehiculo():
    def __init__(self, color, ruedas):
            self.color = color
            self.ruedas = ruedas
    def __str__(self):
        return "Color {}, {} ruedas".format( self.color, self.ruedas )

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        Vehiculo.__init__(self, color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return Vehiculo.__str__(self) + ", {} km/h, {} cc".format(self.velocidad, self.cilindrada)

    def set_velocidad(self, velocidad):
        self.velocidad = velocidad
    def get_velocidad(self):
        return self.velocidad

    def set_cilindrada(cilindrada, self):
        self.cilindrada = cilindrada
    def get_cilindrada(self):
        return self.cilindrada

class Bicicleta(Vehiculo):
    def __init_subclass__(cls) -> None:
        return super().__init_subclass__()
    
    def __str__(self):
        return super().__str__()
    
    def set_tipo():
        

class Camioneta(Vehiculo):
    def 

