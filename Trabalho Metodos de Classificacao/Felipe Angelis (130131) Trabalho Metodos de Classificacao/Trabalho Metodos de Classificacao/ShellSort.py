import time
import random

def shell_sort(arr):
    n = len(arr)
    gap = n // 2  
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2  

def medir_tempo():
    tamanhos = [1000, 5000, 10000]  
    for tamanho in tamanhos:
        print(f"\nTamanho do vetor: {tamanho}")

        crescente = list(range(tamanho))
        inicio = time.time()
        shell_sort(crescente)
        fim = time.time()
        print(f"Tempo para crescente: {fim - inicio:.6f} segundos")
        
        decrescente = list(range(tamanho, 0, -1))
        inicio = time.time()
        shell_sort(decrescente)
        fim = time.time()
        print(f"Tempo para decrescente: {fim - inicio:.6f} segundos")
     
        aleatorio = [random.randint(1, tamanho) for _ in range(tamanho)]
        inicio = time.time()
        shell_sort(aleatorio)
        fim = time.time()
        print(f"Tempo para aleatório: {fim - inicio:.6f} segundos")


medir_tempo()
