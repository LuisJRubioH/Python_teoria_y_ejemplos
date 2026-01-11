from exceptions import LibroNoDisponibleError
from exceptions import UsuarioNoEncontradoError

class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []
        self.usuarios = []

    def libros_disponibles(self):
        return [libro for libro in self.libros if libro.disponible]
    
    def buscar_usuario(self, cedula: str):
        for usuario in self.usuarios:
            if usuario.cedula == cedula:
                return usuario
        raise UsuarioNoEncontradoError(f"El usuario con la cédula {cedula} no fue encontrado.")


    def buscar_usuario(self, cedula):
        for usuario in self.usuarios:
            if usuario.cedula == cedula:
                return usuario
        raise UsuarioNoEncontradoError(f"El usuario con la cédula {cedula} no fue encontrado.")
    
    def buscar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo == titulo:
                return libro
        raise LibroNoDisponibleError(f"El libro con el título {titulo} no fue encontrado.")
    
    @staticmethod
    def validar_isbn(isbn):
        len(isbn) >= 10
