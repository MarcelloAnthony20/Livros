def conta_itens_recursiva(lista:list)->int:
    '''
    Essa função retorna tamanho de uma lista de maneira recursiva.

    Parâmetros:
        lista(list): Uma lista de elementos.
    Retorna:
        int: Tamanho da lista.
    '''
    if lista == []:
        return 0
    lista.pop()
    return 1 + conta_itens_recursiva(lista)

def test_conta_itens_recursiva():
    assert conta_itens_recursiva([]) == 0
    assert conta_itens_recursiva([42]) == 1
    assert conta_itens_recursiva([1, 2, 3, 4, 5]) == 5
    assert conta_itens_recursiva([7, 7, 7]) == 3
    assert conta_itens_recursiva([1, "a", 3.14, True]) == 4
    assert conta_itens_recursiva(list(range(100))) == 100
    assert conta_itens_recursiva([1, [2, 3], 4]) == 3
    print("✅ conta_itens_recursiva: Todos os testes passaram!")

test_conta_itens_recursiva()