import time
import random

def quick_sort(arr):
    if len(arr) <= 1:
        return arr  
    else:
        pivot = arr[len(arr) // 2] 
        menores = [x for x in arr if x < pivot] 
        iguais = [x for x in arr if x == pivot]  
        maiores = [x for x in arr if x > pivot] 
        return quick_sort(menores) + iguais + quick_sort(maiores)

def medir_tempo():
    tamanhos = [1000, 5000, 10000]  #
    for tamanho in tamanhos:
        print(f"\nTamanho do vetor: {tamanho}")

        crescente = list(range(tamanho))
        inicio = time.time()
        quick_sort(crescente)
        fim = time.time()
        print(f"Tempo para crescente: {fim - inicio:.6f} segundos")

        decrescente = list(range(tamanho, 0, -1))
        inicio = time.time()
        quick_sort(decrescente)
        fim = time.time()
        print(f"Tempo para decrescente: {fim - inicio:.6f} segundos")

        aleatorio = [random.randint(1, tamanho) for _ in range(tamanho)]
        inicio = time.time()
        quick_sort(aleatorio)
        fim = time.time()
        print(f"Tempo para aleatório: {fim - inicio:.6f} segundos")

medir_tempo()
