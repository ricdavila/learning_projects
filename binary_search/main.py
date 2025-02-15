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
    
    # define os valores do intervalo caso não sejam dados
    if maximo == None:
        maximo = len(lista) - 1
    if minimo == None:
        minimo = lista[0]

    # define a casa do valor do meio
    mid = (maximo + minimo) // 2

    # >>> exibir o intervalo a cada iteração #
    print(f"min: {minimo} -- mid: {mid} -- max: {maximo}")

    # quando o valor não está na lista dada, o código chega no paradoxo max < min. 
    # Assim, somente realizamos a busca enquanto max >= min, evitando continuar 
    # infinitamente caso o valor esteja ausente

    # "qual alvo que permite max == min?" isto ocorre quando o alvo em questão for
    # o MAIOR ou o MENOR valor do conjunto inicial

    if maximo >= minimo:
        # caso o valor central seja o alvo, encerra a busca
        if lista[mid] == alvo:
            return mid
        # caso o valor central seja MAIOR que o alvo, reduz o intervalo de busca,
        # excluindo o valor central (max = mid-1)
        elif lista[mid] > alvo:
            return binary_search(lista, alvo, mid - 1, minimo)
        # caso o valor central seja MENOR que o alvo, reduz o intervalo, excluindo
        # também o valor central (min = mid+1)
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