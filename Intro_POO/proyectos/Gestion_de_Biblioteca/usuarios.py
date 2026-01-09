class Usuario:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula
        self.libros_prestados = []

    def solicitar_libro(self, titulo):
        return f"Solicitud de libro '{titulo}' realizada"


class Estudiante(Usuario):
    def __init__(self,nombre, cedula, carrera):
        super().__init__(nombre, cedula)
        self.carrera = carrera
        self.limite_prestamos = 3
        

    def solicitar_libro(self, titulo):
        if len(self.libros_prestados) < 3:
            self.libros_prestados.append(titulo)
            return f"Prestamo del libro: {titulo} autorizado"
        else:
            return f"Límite de libros prestados alcanzado {self.limite_prestamos}. No puedes prestar más librros"



class Profesor(Usuario):
    def __init__(self, nombre, cedula):
        super().__init__(nombre, cedula)
        self.limite_prestamos = None

    def splicitar_libro(self, titulo):
        return f"Prestamo del libro: {titulo} autorizado"
    
# Ejemplo de uso de las clases Usuario, Estudiante y Profesor
estudiante = Estudiante("Ana Gomez", "12345678", "Ingeniería")
profesor = Profesor("Dr. Luis Perez", "87654321")

print(estudiante.solicitar_libro("Cien años de soledad"))
print(estudiante.solicitar_libro("Don Quijote de la Mancha"))
print(estudiante.solicitar_libro("La Odisea"))
print(estudiante.solicitar_libro("El Principito")) # Debería indicar que se ha alcanzado el límite

print(profesor.solicitar_libro("El principito"))
print(profesor.solicitar_libro("1984"))
print(profesor.solicitar_libro("El quijote"))
print(profesor.solicitar_libro("La biblia"))
