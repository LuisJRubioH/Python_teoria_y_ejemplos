# Declaración de la clase
class Usuario():
    
    # atributo de clasle
    hora_inicio_sesion = None
    
    # atributos de instancia
    def __init__(self, nombre: str, apellido:str, email:str) -> None:
        self.nombre  = nombre
        self.apellido = apellido
        self.email = email

    # métodos
    def inicio_sesion(self):
        print(f"El usuario {self.nombre} ha iniciado sesión")
    
    def fin_sesion(self):
        print(f"El usuario {self.nombre} ha finalizado su sesión")
        
# creación de objetos o instancias

usuraio1 = Usuario("Luis", "Rubio", "luisrubio@email.com")

usuraio2 = Usuario("Ori", "Giraldo", "origiraldo@email.com")

usuraio1.inicio_sesion()
usuraio2.inicio_sesion()

usuraio1.fin_sesion()
usuraio2.fin_sesion()

