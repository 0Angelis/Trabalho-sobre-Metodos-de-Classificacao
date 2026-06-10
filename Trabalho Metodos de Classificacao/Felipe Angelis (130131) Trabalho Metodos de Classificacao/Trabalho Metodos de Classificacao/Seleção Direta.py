import time
import random

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        menor_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[menor_idx]:
                menor_idx = j
        
        arr[i], arr[menor_idx] = arr[menor_idx], arr[i]

def medir_tempo():
    tamanhos = [1000, 5000, 10000]  
    for tamanho in tamanhos:
        print(f"\nTamanho do vetor: {tamanho}")

        crescente = list(range(tamanho))
        inicio = time.time()
        selection_sort(crescente)
        fim = time.time()
        print(f"Tempo para crescente: {fim - inicio:.6f} segundos")

        decrescente = list(range(tamanho, 0, -1))
        inicio = time.time()
        selection_sort(decrescente)
        fim = time.time()
        print(f"Tempo para decrescente: {fim - inicio:.6f} segundos")

        aleatorio = [random.randint(1, tamanho) for _ in range(tamanho)]
        inicio = time.time()
        selection_sort(aleatorio)
        fim = time.time()
        print(f"Tempo para aleatório: {fim - inicio:.6f} segundos")


medir_tempo()
