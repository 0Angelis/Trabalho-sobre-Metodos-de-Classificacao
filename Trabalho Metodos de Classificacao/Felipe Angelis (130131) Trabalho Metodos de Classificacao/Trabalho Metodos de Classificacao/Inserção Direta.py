import time
import random

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def medir_tempo():
    tamanhos = [1000, 5000, 10000]  
    for tamanho in tamanhos:
        print(f"\nTamanho do vetor: {tamanho}")

        crescente = list(range(tamanho))
        inicio = time.time()
        insertion_sort(crescente)
        fim = time.time()
        print(f"Tempo para crescente: {fim - inicio:.6f} segundos")

        decrescente = list(range(tamanho, 0, -1))
        inicio = time.time()
        insertion_sort(decrescente)
        fim = time.time()
        print(f"Tempo para decrescente: {fim - inicio:.6f} segundos")

        aleatorio = [random.randint(1, tamanho) for _ in range(tamanho)]
        inicio = time.time()
        insertion_sort(aleatorio)
        fim = time.time()
        print(f"Tempo para aleatório: {fim - inicio:.6f} segundos")


medir_tempo()
