import time
import random


def heapify(arr, n, i):
    maior = i  
    esquerda = 2 * i + 1  
    direita = 2 * i + 2 

    if esquerda < n and arr[esquerda] > arr[maior]:
        maior = esquerda

    if direita < n and arr[direita] > arr[maior]:
        maior = direita

    if maior != i:
        arr[i], arr[maior] = arr[maior], arr[i]  
        heapify(arr, n, maior)  

def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  
        heapify(arr, i, 0)  

def medir_tempo():
    tamanhos = [1000, 5000, 10000]
    for tamanho in tamanhos:
        print(f"\nTamanho do vetor: {tamanho}")

        crescente = list(range(tamanho))
        inicio = time.time()
        heap_sort(crescente)
        fim = time.time()
        print(f"Tempo para crescente: {fim - inicio:.6f} segundos")
    
        decrescente = list(range(tamanho, 0, -1))
        inicio = time.time()
        heap_sort(decrescente)
        fim = time.time()
        print(f"Tempo para decrescente: {fim - inicio:.6f} segundos")

        aleatorio = [random.randint(1, tamanho) for _ in range(tamanho)]
        inicio = time.time()
        heap_sort(aleatorio)
        fim = time.time()
        print(f"Tempo para aleatório: {fim - inicio:.6f} segundos")

medir_tempo()
