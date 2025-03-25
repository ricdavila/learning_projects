# algoritmo de busca binária

def binary_search(lista, alvo, maximo=None, minimo=None):
    """
    Realiza uma busca binária, reduzindo pela metade o intervalo de pesquisa
    a cada iteração do código. Isto é, reduz a pesquisa de forma exponencional.

    Parâmetros:
    > lista : conjunto onde será feita a busca
    > alvo : valor que está sendo buscado

    Retorna:
    > o índice do alvo dentro da lista, quando o valor for encontrado
    > -1, quando o alvo não for encontrado na lista
    """

    # define os limites do intervalo, caso não sejam dados
    if maximo == None:
        maximo = len(lista) - 1
    if minimo == None:
        minimo = lista[0]

    # encontra o valor central
    mid = (maximo + minimo) // 2

    # realiza a busca, enquanto o intervalo min-max for válido
    if maximo >= minimo:
        # caso o valor central seja o alvo, encerra a busca
        if lista[mid] == alvo:
            return mid
        # caso valor central seja maior que o alvo
        elif lista[mid] > alvo:
            return binary_search(lista, alvo, mid - 1, minimo)
        # caso o valor central seja menor que o alvo
        else:
            return binary_search(lista, alvo, maximo, mid + 1)
    
    # caso max < min, o valor não encontra-se na lista
    else:
        return -1

if __name__ == "__main__":

    # cria uma lista de tamanho dado pelo range
    lista = list(range(10000))

    # valor a ser encontrado dentro da lista acima
    alvo = 150

    # realiza a busca e printa o index do alvo
    print(f"\n> INDEX DO VALOR PROCURADO: {binary_search(lista, alvo)}")