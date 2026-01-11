
class Libro:
    #  definimos los atribustos de instancia
    def  __init__(self, titulo, autor, isbn, disponible = True):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = disponible
        self.__veces_prestado = 0
    
    # contruimos los métodos de instancia

    def __str__(self):
        return f"{self.titulo} por {self.autor}, disponible: {self.disponible}"


    def prestar(self):
        if self.disponible:
            self.disponible = False
            self.__veces_prestado += 1
            return f"El libro '{self.titulo}' fue prestado exitosamente- Total prestamos: {self.__veces_prestado}"
        return f"El libro '{self.titulo}' no está disponible para préstamo"

    def devolver(self):
        self.disponible = True
        return f"El libro '{self.titulo}' ha sido devuelto y disponible nuevamente"

    def espopular(self):
        return self.veces_prestado > 5
#  método getter para veces_prestado
    def get_veces_prestado(self):
        return self.__veces_prestado

    def set_veces_prestado(self, veces_prestado):
        self.__veces_prestado = veces_prestado


# Ejemplo de uso de la clase Libro

mi_libro = Libro("Cien años de soledad", "Gabriel Garcia Márquez", "978-3-16-148410-0", True)
otro_libro = Libro("Pedro Páramo", "Juan Rulfo", "978-1-23-456789-0", True)

print(mi_libro.prestar())
print(mi_libro.devolver())


mi_libro.set_veces_prestado(6)
print(mi_libro.get_veces_prestado())

catalogo = [mi_libro, otro_libro]

for libro in catalogo:
    print(libro)

