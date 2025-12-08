def busca_binaria(lista:list, alvo:int) -> int | None:
    '''
    Realiza uma busca binária em uma lista ordenada para encontrar o índice do elemento alvo.

    Parâmetros:
        lista (list): Uma lista ordenada de elementos.
        alvo (int): O elemento que se deseja encontrar na lista.

    Retorna:
        int | None: O índice do elemento alvo ou None se não for encontrado.
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

def test_busca_binaria():
    assert busca_binaria([1,2,3,4,5],5) == 4
    assert busca_binaria([1,2,3,4,5],6) == None
    assert busca_binaria(['a','b','c','d','e'],'c') == 2
    print("✅ test_selection_sort: Todos os testes passaram!")

test_busca_binaria()