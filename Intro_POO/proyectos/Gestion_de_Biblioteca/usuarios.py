from abc import ABC, abstractmethod
from typing import Protocol
from exceptions import TituloInvalidoError



class SolicitanteProtocol(Protocol):
    def prestar_libro(self) -> str:
        """
        Método que debe implementar cualquier clase que quiera solicitante.
        """
        ...

class UsuarioBase(ABC):
    @abstractmethod
    def solicitar_libro(self):
        pass

class Usuario(UsuarioBase):
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
        if not titulo:
            raise TituloInvalidoError(f"El libro con el título {titulo} no existe en la biblioteca.")
        if len(self.libros_prestados) < 3:
            self.libros_prestados.append(titulo)
            return f"Prestamo del libro: {titulo} autorizado"
        else:
            return f"Límite de libros prestados alcanzado {self.limite_prestamos}. No puedes prestar más librros"

class Profesor(Usuario):
    def __init__(self, nombre, cedula):
        super().__init__(nombre, cedula)
        self.limite_prestamos = None

    def solicitar_libro(self, titulo):
        return f"Prestamo del libro: {titulo} autorizado"
    
