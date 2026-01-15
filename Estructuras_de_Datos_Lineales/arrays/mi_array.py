class MiArray:
    def __init__(self, capacity, fill_value=None):
        self.items = list()
        for i in range(capacity):
            self.items.append(fill_value)

    # cntruimos algunos métodos privados para nuestra clase
    
    # definimos el tamaño del array como un método privado
    def __len__(self):
        return len(self.items)
    
    # representamos como strings sus elementos
    def __str__(self):
        return str(self.items)
    
    # definimos u iterador
    def __iter__(self):
        return iter(self.items)
    
    # método para obtener eklementos del array
    def __getitem__(self, index):
        return self.items[index]

    # método para modificar u elemento
    def __setitem__(self, index, new_item):
        self.items[index] = new_item
