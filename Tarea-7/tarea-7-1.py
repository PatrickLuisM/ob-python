class Vehiculo:
    color = ""
    ruedas = 0
    puertas = 0

    def colorVeh(self):
        print(self.color)
    
    def ruedasVeh(self):
        print(self.ruedas)
    
    def puertasVeh(self):
        print(self.puertas)


class Coche(Vehiculo):
    velocidad = 0.00
    cilindrada = True

    def velCoc(self):
        print(self.velocidad)
    
    def cilinCoc(self):
        print(self.cilindrada)


coche = Coche()
coche.color = "Negro"
coche.puertas = 4
coche.ruedas = 8
coche.velocidad = 120.00
coche.cilindrada = False

coche.colorVeh()
coche.puertasVeh()
coche.ruedasVeh()
coche.cilinCoc()
coche.velCoc()
