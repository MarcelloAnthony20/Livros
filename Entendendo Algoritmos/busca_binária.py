def busca_binaria(lista:list, alvo:int) -> int:
    '''
    Realiza uma busca binária em uma lista ordenada para encontrar o índice do elemento alvo.

    Parâmetros:
    lista (list): Uma lista ordenada de elementos.
    alvo (int): O elemento que se deseja encontrar na lista.

    Retorna:
    int: O índice do elemento alvo na lista, ou null se o elemento não for encontrado.
    '''

    esquerda = 0
    direita = len(lista) - 1

    while esquerda <= direita:
        meio = (esquerda + direita)//2
        if alvo == lista[meio]:
            return meio
        elif alvo < lista[meio]:
            direita = meio - 1
        else:
            esquerda = meio + 1

    return None

print(busca_binaria([1,2,3,4,5],6))