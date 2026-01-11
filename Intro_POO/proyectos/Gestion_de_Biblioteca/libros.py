from exceptions import LibroNoDisponibleError
from typing import Protocol

class LibroProtocol(Protocol):
    def prestar(self) -> str:
        """
        Método que debe implementar cualquier clase que quiera solicitante.
        """
        ...

    def devolver(self) -> str:
        """
        Método que debe implementar cualquier clase que quiera solicitante.
        """
        ...

    def calcular_duracion(self) -> str:
        """
        Método que debe implementar cualquier clase que quiera solicitante.
        """
        ...

class Libro:
    #  definimos los atribustos de instancia
    def  __init__(self, titulo, autor, isbn, disponible = True):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = disponible
        self.__veces_prestado = 0
    
    @staticmethod
    def crear_no_disponible(cls, titulo, autor, isbn):
        return cls(titulo, autor, isbn, disponible = False )
    # contruimos los métodos de instancia

    def __str__(self):
        return f"{self.titulo} por {self.autor}, disponible: {self.disponible}"

    def prestar(self):
        if not self.disponible:
            raise LibroNoDisponibleError(f"El libro '{self.titulo}' no está disponible para préstamo.")

        if self.disponible:
            self.disponible = False
            self.__veces_prestado += 1
            return f"El libro '{self.titulo}' fue prestado exitosamente- Total prestamos: {self.__veces_prestado}"
        return f"El libro '{self.titulo}' no está disponible para préstamo"

    def devolver(self):
        self.disponible = True
        return f"El libro '{self.titulo}' ha sido devuelto y disponible nuevamente"
    
    @property
    def espopular(self):
        return self.veces_prestado > 5

    @property
    def veces_prestado(self):
        return self.__veces_prestado
    @veces_prestado.setter
    def veces_prestado(self, veces_prestado):
        if veces_prestado > 0:
            self.__veces_prestado = veces_prestado
        raise ValueError("El número de veces prestado debe ser mayor que cero.")

    @property
    def descripcion_completa(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, ISBN: {self.isbn}, Disponible: {self.disponible}"



class LibroFisico(Libro):
    def calcular_duracion(self):
        return "7 días"

class LibroDigital(Libro):
    def calcular_duracion(self):
        return "14 días"