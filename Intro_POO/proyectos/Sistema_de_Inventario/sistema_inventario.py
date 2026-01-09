class Producto:
    
    def __init__(self, id:int, nombre:str, precio:float, cantidad:int):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def __str__(self):
        return f"{self.nombre} - (ID:{self.id}) - Precio: ${self.precio} - Stokc: {self.cantidad}"

class Inventario:

    def __init__(self):
        self.productos = {}
        
    def agregar_producto(self, producto):
        if producto.id in self.productos:
            print("Producto ya existe. Actualizando cantidad...")
            self.productos[producto.id].cantidad += producto.cantidad
        
        else:
            self.productos[producto.id] = producto
            print("Producto agregado al inventario exitosamente.")


    def eliminar_producto(self,id): 
        if id in self.productos:
            del self.productos[id]
            print(f"Producto con ID {id} eliminado")
        else:
            print(f"producto con con ID {id} no encontrado")


    def listar_productos(self):
        for producto in self.productos.values():
            print(producto)
          
            
    def actualizar_producto(self, id , cantidad=None, precio=None):
        if id in self.productos:
            if cantidad is not None:
                self.productos[id].cantidad = cantidad
            if precio is not None:
                self.productos[id].precio = precio
            print(f"Producto con ID {id} actualizado")
        else:
            print("producto no encontrado")
            
            
    

inventario = Inventario()
producto1 = Producto(1,"MANZANA", 0.50, 100)
producto2 = Producto(2,"NARANJAS", 0.30, 150)



print(producto1)
print(producto2)

inventario.agregar_producto(producto1)
inventario.agregar_producto(producto2)
inventario.agregar_producto(producto1)

inventario.listar_productos()

inventario.actualizar_producto(1,cantidad=1000, precio=0.45)
inventario.listar_productos()

inventario.eliminar_producto(2)
inventario.listar_productos()
