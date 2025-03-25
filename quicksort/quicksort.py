"""
Implementação do algoritmo Quicksort, por Ricardo d'Avila.
Github: https://github.com/ricdavila
"""

def quicksort(lista):
    
    # caso-base
    if len(lista) < 2:
        return lista

    # definição do pivô
    pivo = lista[0]
    # particionamento da lista em dois subarrays de elementos
    esquerda = [i for i in lista[1:] if i <= pivo] # partição com os menores ou iguais ao pivô
    direita = [i for i in lista[1:] if i > pivo] # partição com os maiores que o pivô

    # ordena os subarrays e retorna a lista ordenada
    return quicksort(esquerda) + [pivo] + quicksort(direita)

if __name__ == "__main__":
    # teste do algoritmo
    lista_teste = [30, 12, 41, 4, 1, 4, 10, 9]
    #print(quicksort(lista_teste))