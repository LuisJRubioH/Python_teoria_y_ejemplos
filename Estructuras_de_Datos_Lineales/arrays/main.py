from mi_array import MiArray
from grid import Grid

def main():
    menu = MiArray(5)

    """usando los méros propios de python"""
    print(len(menu))
    print(menu)
    #agregamos elementos a la lsita
    for i in range(len(menu)):
        menu[i] = i + 1
    print(menu)

    """usando los métodos creados por nosotros"""
    #Creamos una isntancia (u objeto)
    mi_lista = MiArray(7)

    #usamos el método __len__ para ver su longitud 
    print(mi_lista.__len__())

    # usamos el atriibuto items para ver los elementos de la lista
    print(mi_lista.items)

    #usamos el método __setitem__ para reemplazar los elementos de l alista 
    for i in range(mi_lista.__len__()):
        mi_lista.__setitem__(i, i*2)
    print(mi_lista.items)

    #usamos el método __getitem__ para encontra un elemnto en una posición(index) deternminda 
    print(mi_lista.__getitem__(4))

    #XCreamos una istancia de la clase grid
    mi_matrix = Grid(4,5)
    print(mi_matrix)
    print(mi_matrix.get_height())
    print(mi_matrix.get_width())

    for raw in range(mi_matrix.get_height()):
        for col in range(mi_matrix.get_width()):
            mi_matrix[raw][col] = raw * col
    
    print(mi_matrix)
    print(mi_matrix.__getitem__(2)[3])

if __name__ == "__main__":
    main()