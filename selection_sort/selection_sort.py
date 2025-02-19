"""
Sistema de Ordenação por Seleção, por Ricardo d'Avila.
Github: https://github.com/ricdavila
"""

def ordenar_lista(lista):
    """Ordena a lista dada com o algoritmo de Ordenação por Seleção — Complexidade O(n²)."""

    lista_ordenada = []
    # para cada elemento da lista, encontra o menor valor e o adiciona à lista ordenada
    for i in range(len(lista)):
        menor = buscar_menor(lista) # encontra o menor valor no restante da lista
        lista_ordenada.append(lista.pop(menor)) # adiciona o valor à nova lista e o remove da lista antiga
    
    return lista_ordenada # retorna a nova lista


def buscar_menor(lista):
    """Algoritmo para encontrar o indíce do menor elemento da lista."""

    menor = 0

    for i in range(len(lista)):
        # atualiza o valor do menor índice caso necessário
        if lista[i] < lista[menor]:
            menor = i

    return menor # retorna o índice do menor valor encontrado


if __name__ == '__main__':
    # teste
    listagem = [0, 50, 241, 40, 10, 1, 4, 7, 2, 3]
    print(ordenar_lista(listagem))




