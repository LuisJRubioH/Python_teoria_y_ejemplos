class BibliotecaError(Exception):
    """Clase base para excepciones de la biblioteca."""
    pass

class TituloInvalidoError(BibliotecaError):
    """Excepción para títulos de libros inválidos."""
    pass

class UsuarioNoEncontradoError(Exception):
    """Excepción para usuarios no encontrados."""
    pass

class LibroNoDisponibleError(Exception):
    """Excepción para libros no disponibles."""
    pass
