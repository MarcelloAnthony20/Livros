def quick_sort(lista:list)->list:
    '''
    Está função ordena os valores de uma lista.
    
    Parâmetros:
        lista(list): Uma lista de elementos.
    Retorna:
        list: Uma lista de elementos ordenados.
    '''
    if len(lista)<2:
        return lista
    else:
        pivo = lista[0]
        menores = [i for i in lista[1:] if i <= pivo]
        maiores = [i for i in lista[1:] if i > pivo]
        return quick_sort(menores) + [pivo] + quick_sort(maiores)


def test_quick_sort():
    assert quick_sort([2, 6, 8, 5, 98, 4, 2]) == [2, 2, 4, 5, 6, 8, 98]
    assert quick_sort([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert quick_sort([9, 8, 7, 6, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert quick_sort(['a', 'c', 'u', 'j', 'o', 'i']) == ['a', 'c', 'i', 'j', 'o', 'u']
    print("✅ test_quick_sort: Todos os testes passaram!")

test_quick_sort()