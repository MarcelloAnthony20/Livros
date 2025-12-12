def busca_no_menor_custo(tabela_custos:dict, processados:list)->str | None:
    '''
    Encontra o nó com menor custo que ainda não foi processado.

    Parâmetros:
        tabela_custos (dict): Dicionário onde as chaves são nós e os valores são custos.
        processados (list): Lista de nós já processados.

    Retorna:
        str | None: O nó com menor custo ou None se todos os nós já foram verificados.
    '''

    menor = float('inf')
    menor_no = None
    
    for no in tabela_custos:
        if tabela_custos[no] < menor and no not in processados:
            menor = tabela_custos[no]
            menor_no = no
    return menor_no

def test_busca_no_menor_custo():
    custos = {'a': 6, 'b': 2, 'fim': 10}
    processados = []
    
    assert busca_no_menor_custo(custos, processados) == 'b'
    processados.append('b')
    assert busca_no_menor_custo(custos, processados) == 'a'
    processados.append('a')
    assert busca_no_menor_custo(custos, processados) == 'fim'
    processados.append('fim')
    assert busca_no_menor_custo(custos, processados) == None
    print("✅ test_busca_no_menor_custo: Todos os testes passaram!")

test_busca_no_menor_custo()