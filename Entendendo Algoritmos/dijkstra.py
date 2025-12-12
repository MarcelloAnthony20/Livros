from busca_no_menor_custo import busca_no_menor_custo
def djikstra(tabela_custos,tabela_vizinhos,tabela_pais):
    '''
    Essa função é um implementação do algoritmo de djikstra

    Parâmetros:
        tabela_custos (dict): Dicionário com os custos para chegar a cada nó.
        tabela_vizinhos (dict): Dicionário com os vizinhos e pesos de cada nó.
        tabela_pais (dict): Dicionário com o nó pai de cada nó no caminho mais curto.

    Retorna:
        None: A função modifica as tabelas de custos e pais
    '''
    processados = []
    no = busca_no_menor_custo(tabela_custos,processados)
    while no:
        custo = tabela_custos[no]
        for vizinho in tabela_vizinhos[no]:
            novo_custo = custo + tabela_vizinhos[no][vizinho]
            if novo_custo < tabela_custos[vizinho]:
                tabela_custos[vizinho] = novo_custo
                tabela_pais[vizinho] = no 

        processados.append(no)
        no = busca_no_menor_custo(tabela_custos,processados)


def test_djikstra():
    tabela_custos = {'a': 6, 'b': 2, 'fim': float('inf')}
    tabela_vizinhos = {
        'inicio': {'a': 6, 'b': 2},
        'a': {'fim': 1},
        'b': {'a': 3, 'fim': 5},
        'fim': {}
    }
    tabela_pais = {'a': None, 'b': None, 'fim': None}
    
    djikstra(tabela_custos, tabela_vizinhos, tabela_pais)
    
    assert tabela_custos['a'] == 5
    assert tabela_custos['b'] == 2
    assert tabela_custos['fim'] == 6
    assert tabela_pais['a'] == 'b'
    assert tabela_pais['b'] == None
    assert tabela_pais['fim'] == 'a'
    
    tabela_custos2 = {'b': 10, 'c': 20, 'd': float('inf')}
    tabela_vizinhos2 = {
        'a': {'b': 10, 'c': 20},
        'b': {'c': 5, 'd': 15},
        'c': {'d': 10},
        'd': {}
    }
    tabela_pais2 = {'b': None, 'c': None, 'd': None}
    
    djikstra(tabela_custos2, tabela_vizinhos2, tabela_pais2)
    
    assert tabela_custos2['b'] == 10
    assert tabela_custos2['c'] == 15
    assert tabela_custos2['d'] == 25
    assert tabela_pais2['b'] == None
    assert tabela_pais2['c'] == 'b'
    assert tabela_pais2['d'] == 'b'
    
    print("✅ test_djikstra: Todos os testes passaram!")

test_djikstra()
