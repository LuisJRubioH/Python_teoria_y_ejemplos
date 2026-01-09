class Ciudadano():
    def __init__(self, nombre, profesion):
        self.nombre = nombre
        self.profesion = profesion
        
    def saludar(self):
        print(f"Hola, soy {self.nombre}. Mi profesion {self.profesion}")
        
        
class Medico(Ciudadano):
    def __init__(self, nombre):
        super().__init__(nombre, "Medico")
        
class Policia(Ciudadano):
    def __init__(self, nombre):
        super().__init__(nombre, "Policia")
        

        

persona1 = Ciudadano("Ana", "Informatica")
persona2 = Medico("Javier")
persona3 = Policia("Raul")

persona1.saludar()
persona2.saludar()
persona3.saludar()
