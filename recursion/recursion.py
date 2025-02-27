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


if __name__ == "__main__" :
    # teste  
    print(euclides(640, 1680))