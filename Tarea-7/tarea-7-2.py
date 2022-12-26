class Alumno:
    nombre = ""
    nota = 0.00

    def __init__(self,nombre,nota) -> None:
        self.nombre = nombre
        self.nota = nota

    def condicion(self):
        if self.nota < 11:
            print("Nota",self.nota, "esta desaprobado")
        else:
            print("Nota",self.nota, "esta aprobado")


alumn = Alumno("Patrick",15.00)

alumn.condicion()
