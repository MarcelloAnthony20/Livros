def busca_binaria_recursiva(lista:list, alvo:int, esquerda:int=0, direita:int=None)->int | None:
    '''
    Realiza uma busca binária em uma lista ordenada para encontrar o índice do elemento alvo.

    Parâmetros:
        lista (list): Uma lista ordenada de elementos.
        alvo (int): O elemento que se deseja encontrar na lista.
        esquerda (int): Índice inicial da busca (padrão: 0).
        direita (int): Índice final da busca (padrão: len(lista)-1).

    Retorna:
        int | None: O índice do elemento alvo ou None se não for encontrado.
    '''
    if direita is None:
        direita = len(lista) - 1
    if esquerda > direita:
        return None
    
    meio = (esquerda + direita) // 2
    
    if lista[meio] == alvo:
        return meio
    elif alvo < lista[meio]:
        return busca_binaria_recursiva(lista, alvo, esquerda, meio - 1)
    else:
        return busca_binaria_recursiva(lista, alvo, meio + 1, direita)

print(busca_binaria_recursiva([1,2,3,4,5],5))
def test_busca_binaria_recursiva():
    assert busca_binaria_recursiva([1,2,3,4,5],5) == 4
    assert busca_binaria_recursiva([1,2,3,4,5],6) == None
    assert busca_binaria_recursiva(['a','b','c','d','e'],'c') == 2
    print("✅ busca_binaria: Todos os testes passaram!")

test_busca_binaria_recursiva()