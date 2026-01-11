import os
import sys

from datetime import datetime

from bubble_sort import bubble_sort
from selection_sort import selection_sort



def main():

    with open(r".\data\numeros.csv", "r", encoding="utf-8-sig") as f:
        line = f.readline()
        arr1 = list(map(int, line.strip().split(',')))


    arr2 = arr1.copy()

   # print("Array original:", arr1)
    print("*"*40)
    
    start_time = datetime.now()
    sorted_arr1 = bubble_sort(arr1)
    end_time = datetime.now()
    #print("Sorted array using Bubble Sort:", sorted_arr1)
    print("Bubble Sort Time taken:", end_time - start_time)

    print("*"*40)

    start_time = datetime.now()
    sorted_arr2 = selection_sort(arr2)
    end_time = datetime.now()
    #print("Sorted array using Selection Sort:", sorted_arr2)
    print("Selection Sort Time taken:", end_time - start_time)

if __name__ == "__main__":
    main()
