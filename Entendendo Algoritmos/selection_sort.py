def busca_menor(lista:list,inicio:int)->int:
    '''
    Está função busca e retorna o menor valor em uma lista.

    Paramêtros:
        lista(list): Uma lista de elementos.
        inicio(int): Posição de ínicio de busca.

    Retorna:
        int: o índice do menor valor da lista.
    '''
    menor = inicio
    for i in range(inicio + 1, len(lista)):
        if lista[i] < lista[menor]:
              menor = i
    return menor


def selection_sort(lista:list)->list:
    '''
    Está função ordena os valores de uma lista.
    
    Parâmetros:
        lista(list): Uma lista de elementos.
    Retorna:
        list: Uma lista de elementos ordenados.
    '''
    for i in range(len(lista)):
        indice = busca_menor(lista, i)
        lista[i], lista [indice] = lista[indice], lista[i]
    return lista



def test_busca_menor():
    assert busca_menor([2, 6, 8, 5, 98, 4, 2],0) == 0
    assert busca_menor([1, 2, 3, 4, 5, 6, 7, 8, 9],0) == 0
    assert busca_menor([9, 8, 7, 6, 5, 4, 3, 2, 1],0) == 8
    assert busca_menor(['a', 'c', 'u', 'j', 'o', 'i'],0) == 0
    print("✅ test_busca_menor: Todos os testes passaram!")

def test_selection_sort():
    assert selection_sort([2, 6, 8, 5, 98, 4, 2]) == [2, 2, 4, 5, 6, 8, 98]
    assert selection_sort([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert selection_sort([9, 8, 7, 6, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert selection_sort(['a', 'c', 'u', 'j', 'o', 'i']) == ['a', 'c', 'i', 'j', 'o', 'u']
    print("✅ test_selection_sort: Todos os testes passaram!")

test_busca_menor()
test_selection_sort()
