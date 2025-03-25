"""
Implementações diversas de funções recursivas, por Ricardo d'Avila.
Github: https://github.com/ricdavila
"""

def soma_nat(n):
    """
    Função para soma dos n primeiros números naturais.

    Entrada:
    - n (int) : número natural até o qual será feita a soma.

    Retorno:
    - (int) soma dos números naturais, de 0 até n. 
    """
    
    # caso base
    if n == 1:
        return n
    
    return n + soma_nat(n - 1)

def fat(n):
    """
    Função para fatorar um número natural.
    
    Entrada: 
    - n (int): número natural que será fatorado.

    Retorno:
    - (int) resultado de n!
    """
    
    # caso base
    if n == 1:
        return n
    
    return n * fat(n - 1)

def div(m, n):
    """
    Função para realizar divisões inteiras entre m e n, sem utilizar *, / ou //

    Entrada:
    - m (int) : número a ser dividido (dividendo)
    - n (int) : número que dividirá (divisor)

    Retorna:
    - (int) o resultado inteiro da divisão (m / n)
    """
    # caso base
    if m < n:
        return 0
    # caso recursivo
    else:
        return 1 + div(m - n, n)

def collatz(n):
    """
    Calcula o número de chamadas necessárias para que um número natural n
    atinja 1, seguindo as regras da Conjectura de Collatz.

    A Conjectura segue o seguinte método:
    Se o valor for par, divide-o por 2 (n / 2); se o valor for ímpar, multiplica-o por
    3 e então soma-se 1 (3 * n + 1). Repete-se esse processo até que 'n' seja igual a 1.

    Entrada: 
    - n (int) : número natural que será reduzido a 1 pela Conjuctura de Collatz

    Retorna:
    - (int) o número de iterações para que 'n' torne-se 1
    """
    
    # caso base
    if n == 1:
        return 0
    
    # caso recursivo
    if n % 2 == 0:
        return 1 + collatz(n / 2)
    else:
        return 1 + collatz(3 * n + 1)

def euclides(a, b):
    """
    Calcula o máximo divisor comum (MDC) entre dois números naturais a partir do 
    Algoritmo de Euclides. Esse método baseia-se na seguinte propriedade do MDC : 
    
    MDC(a, b) = MDC(b, r); sendo 'a' e 'b' dois números naturais diferentes de 0 
    e 'r' sendo o resto da divisão inteira de 'a' por 'b'. Ou seja, (r = a % b) ou 
    (r = a mod b), utilizando a operação módulo. 

    Entrada:
    - a (int), b (int) : números naturais diferentes de 0; os de quem se deseja
    descobrir o MDC

    Retorno:
    - (int) o máximo divisor comum entre 'a' e 'b'
    """

    # caso base
    # se 'b' for igual a zero, significa que 'a' contém o MDC
    if b == 0:
        return a # retorna o MDC encontrado
    
    # caso recursivo
    else:
        # definimos 'a' = 'b' e fazemos com que 'b' = 'a % b' (resto da divisão inteira entre 'a' e 'b')
        return euclides(b, a % b)

def maior(lista):
    """
    Encontra o maior valor dentro de uma determinada lista.

    Entrada:
    - lista : lista a ser percorrida para encontrar o maior valor

    Retorno :
    - o maior termo da lista
    """
    # caso-base
    # faz uma verificação simples para retornar o maior valor caso a lista seja binária
    # (ou seja, possua apenas dois termos)
    if len(lista) == 2:
        return lista[0] if lista[0] > lista[1] else lista[1]
    else:
        # compara sempre o 1° e 2° elemento da lista, removendo o menor e para que, ao
        # fim, sobre apenas o maior valor da lista
        if lista[0] > lista[1]:
            lista.remove(lista[1])
        else:
            lista.remove(lista[0])

        # executa o código novamente, porém, com 1 elemento a menos
        return maior(lista)

def inverter(n, invertido=0):
    """
    Inverte um número natural. Ex: 1234 -> 4321

    Entrada :
    - n (int) : número natural a ser invertido

    Retorno :
    - (int) : número invertido
    """
    # caso-base
    if n == 0:
        return invertido
    
    # a cada iteração, reduz-se 'n' em 1 unidade e aumenta-se 'invertido' em 1 unidade também. 
    # ex com entrada 123: n = 12, invertido = 3; n = 1, invertido = 32; n = 0, invertido = 321
    return inverter(n // 10, invertido * 10 + n % 10)


def fibonacci(n, n1=0, n2=1):
    """
    Retorna o N-ésimo termo da sequência fibonacci.

    Entrada :
    - n (int) : posição do termo na sequência

    Retorno :
    - o N-ésimo termo da sequência
    """
    # caso-base
    if n == 1:
        return n1
    
    # utiliza 'n' como contador regressivo e progride na sequência fibonacci a partir de 'n1'
    # e 'n2'
    return fibonacci(n-1, n2, n1 + n2)


if __name__ == "__main__" :
    # teste  
    print(fibonacci(5))
    #print(inverter(1234567))