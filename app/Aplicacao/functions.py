#calcualr o proximo numero primo a partir de uma entrada do usuar
from math import isqrt


def numero_primo(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for c in range(3, isqrt(n) + 1,  2): # se nao tiver nenhum divisor menor que a raiz, o numero é primo
        if n % c == 0:
            return False
    return True # não encontramos divisor nenhum até a raiz quadrada.

def proximo_primo(x: int) -> int:
    contador = x
    while True:
        if numero_primo(contador) == True:
            if contador == x:  # se o usuario digitar um numero primo, faz com que a saida seja o proximo numero primo
                contador += 1
                numero_primo(contador)
            return contador
        else:
            contador += 1
            

