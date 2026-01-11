import sys

def selection_sort(arr:list):
    
    # recorremos todo nuestro array
    for i in range(len(arr)):

        # buscamos el minimo en el array no ordenado
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # intercambiamos el minimo encontrado con el primer elemento
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr
