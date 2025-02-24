"""
Implementações diversas de funções recursivas, por Ricardo d'Avila.
Github: https://github.com/ricdavila
"""

def soma_nat(n):
    """
    Função para soma dos n primeiros números naturais.

    Entrada:
    - n : número natural até o qual será feita a soma.

    Retorno:
    - soma dos números naturais, de 0 até n. 
    """
    if n == 1:
        return n
    return n + soma_nat(n - 1)

def fat(n):
    """
    Função para fatorar um número natural.
    
    Entrada: 
    - n : número natural que será fatorado.

    Retorno:
    - resultado de n!
    """

    if n == 1:
        return n
    return n * fat(n - 1)

def div(m, n):
    """
    Função para realizar divisões inteiras entre m e n, sem utilizar *, / ou //

    Entrada:
    - m : número a ser dividido (dividendo)
    - n : número que dividirá (divisor)

    Retorna:
    - o resultado inteiro da divisão (m/n)
    """

    if m < n:
        return 0
    else:
        return 1 + div(m - n, n)

def collatz(n):
    """
    Calcula o número de chamadas necessárias para que um número natural n
    atinja 1, seguindo as regras da Conjectura de Collatz.
    """

    if n == 1:
        return 0
    
    if n % 2 == 0:
        return 1 + collatz(n / 2)
    else:
        return 1 + collatz(3 * n + 1)




if __name__ == "__main__" :
    # teste  
    print(collatz(11))