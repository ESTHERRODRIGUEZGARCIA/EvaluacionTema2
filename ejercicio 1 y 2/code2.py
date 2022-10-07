class Alumno():
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
        print("El alumno se ha creado con éxito. ")

    def __str__(self):
        return 


    def calificacion(self):
        if self.nota >= 5 and self.nota <=10:
            print("Alumno aprobado. ")
        elif self.nota < 5:
            print("Alumno suspenso. ")