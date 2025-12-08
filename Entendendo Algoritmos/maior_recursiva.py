def maior_recursiva(lista:list,i=0)->int | None:
    '''
    Esta função recursiva busca o maior elemento em uma lista e retorna seu índice.

    Parâmetros:
        lista(list): Uma lista de elementos.
        i (int): Índice usado internamente pela recursão.
            Não deve ser informado pelo usuário.

    Retorna:
        int | None: índice do maior elemeneto da lista ou None se a lista for vazia.
    '''
    if lista == []:
        return None
    if len(lista) - 1 == i:
        return lista[i]
    maior_do_resto = maior_recursiva(lista, i + 1)
    return lista[i] if lista[i] > maior_do_resto else maior_do_resto
            

def test_maior_recusiva():
    assert maior_recursiva([]) == None
    assert maior_recursiva([10]) == 10
    assert maior_recursiva([1, 5, 3, 9, 2]) == 9
    assert maior_recursiva([99, 1, 2, 3]) == 99
    assert maior_recursiva([1, 2, 3, 50]) == 50
    assert maior_recursiva([-10, -5, -30]) == -5
    assert maior_recursiva([7, 7, 7]) == 7
    assert maior_recursiva([1.5, 3.2, 2.8]) == 3.2
    assert maior_recursiva(list(range(995))) == 994
    print("✅ maior_recursiva: Todos os testes passaram!")

test_maior_recusiva()