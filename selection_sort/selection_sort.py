"""
Sistema de Ordenação por Seleção, por Ricardo d'Avila.
Github: https://github.com/ricdavila
"""

def ordenar_lista(lista):

    n = len(lista) #tamanho da lista

    if n == 1:
        return lista

    # loop externo
    for i in range(n-1):

        menor = i

        # loop interno
        for j in range(i + 1, n):
            if lista[j] < lista [menor]:
                menor = j

        # reposiciona o menor valor
        if menor != i:
            lista[i], lista[menor] = lista[menor], lista[i]

    return lista # retorna a lista ordenada


if __name__ == '__main__':
    # teste
    listagem = [0, 50, 241, 40, 10, 1, 4, 7, 2, 3]
    print(ordenar_lista(listagem))




