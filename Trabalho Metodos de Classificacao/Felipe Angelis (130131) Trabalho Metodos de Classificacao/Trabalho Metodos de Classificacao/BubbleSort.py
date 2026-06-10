import time
import random

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  

def medir_tempo():
    tamanhos = [1000, 5000, 10000]  
    for tamanho in tamanhos:
        print(f"\nTamanho do vetor: {tamanho}")

        crescente = list(range(tamanho))
        inicio = time.time()
        bubble_sort(crescente)
        fim = time.time()
        print(f"Tempo para crescente: {fim - inicio:.6f} segundos")

        decrescente = list(range(tamanho, 0, -1))
        inicio = time.time()
        bubble_sort(decrescente)
        fim = time.time()
        print(f"Tempo para decrescente: {fim - inicio:.6f} segundos")

        aleatorio = [random.randint(1, tamanho) for _ in range(tamanho)]
        inicio = time.time()
        bubble_sort(aleatorio)
        fim = time.time()
        print(f"Tempo para aleatório: {fim - inicio:.6f} segundos")

medir_tempo()
