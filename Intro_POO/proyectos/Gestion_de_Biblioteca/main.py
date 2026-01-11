from biblioteca import Biblioteca
from data import data_libros, data_estudiantes
from exceptions import BibliotecaError
from exceptions import UsuarioNoEncontradoError
from libros import Libro, LibroFisico, LibroDigital
from persistencia import Persistencia
from usuarios import Estudiante, Profesor, SolicitanteProtocol


persistencia = Persistencia()
biblioteca =persistencia.cargar_datos()


print("*"*20)
print("Bienbenido a la Biblioteca Central 📚📚📚")
print("*"*20)
print("📕 Libros disponibles:")
for libro in biblioteca.libros_disponibles():
    print(libro.descripcion_completa)
print()

cedula = input("Ingrese la cédula del usuario: ")
try:
    usuario = biblioteca.buscar_usuario(cedula)
    print(f"CC: {usuario.cedula} - Usuario: {usuario.nombre}")
except UsuarioNoEncontradoError:
    print("El usuario no fue encontrado.")

tirulo = input("Ingrese el título del libro que desea solicitar: ")
try:
    libro = biblioteca.buscar_libro(tirulo)
    mensaje = usuario.solicitar_libro(tirulo)
    print("\n")
    print(mensaje)
    prestamo = libro.prestar()
    print("\n",prestamo)
except UsuarioNoEncontradoError as e:
    print(f"Error: {e}")

persistencia.guardar_datos(biblioteca)