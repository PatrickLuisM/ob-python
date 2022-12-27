f = open("Tarea-9/vehiculo.txt", 'a')

class Vehiculo:
    marca = ""
    precio = 0.00

    def __init__(self,marca,precio) -> None:
        self.marca = marca
        self.precio = precio


veh1 = Vehiculo("Audi",17.0000)
f.write(veh1.marca + "\n")
f.write(str( veh1.precio)+"\n")
f.close()