def soma_array_recursiva(lista:list)->int:
    '''
    Essa função soma os itens de uma lista de forma recursiva.

    Parâmetros:
        lista(list): A lista com os valores a serem somados
    Retorna:
        int: O valor da soma dos valores da lista
    '''
    
    if len(lista) == 0:
        return 0
    else:
        return lista.pop(0) + soma_array_recursiva(lista)

def test_soma_array_recursiva():
    assert soma_array_recursiva([1,2,3]) == 6
    assert soma_array_recursiva([8,5,6,65]) == 84
    assert soma_array_recursiva([]) == 0
    print ('✅ soma_array_recursiva: Todos os testes passaram!')

test_soma_array_recursiva()
