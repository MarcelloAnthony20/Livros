estados = set(['mt','wa','or','id','nv','ut','ca','az'])
estacoes = {}
estacoes['kum'] = set(['id','nv','ut'])
estacoes['kdois'] = set(['wa','id','mt'])
estacoes['ktres'] = set(['or','nv','ca'])
estacoes['kquatro'] = set(['nv','ut'])
estacoes['kcinco'] = set(['ca','az'])


def algoritmo_ganancioso(estados:set, estacoes:dict) -> set:
    '''
    Essa é uma implementação do algoritmo guloso de conjuntos.
    Seleciona o menor conjunto de estações que cobrem todos os estados.

    Parâmetros:
        estados (set): Um conjunto de estados que precisam ser cobertos.
        estacoes (dict): Um dicionário onde as chaves são nomes de estações 
                        e os valores são conjuntos de estados cobertos por cada estação.

    Retorna:
        set: Um conjunto com os nomes das estações escolhidas.
    '''
    estacoes_escolhidas = set()
    while estados:
        melhor_estacao = None
        estados_cobertos = set()
        for estacao, estados_estacao in estacoes.items():
            cobertos = estados & estados_estacao
            if len(cobertos) > len (estados_cobertos):
                melhor_estacao = estacao
                estados_cobertos = cobertos
        estados -= estados_cobertos
        estacoes_escolhidas.add(melhor_estacao)
    return estacoes_escolhidas


def test_algoritmo_ganancioso():
    estados_teste = set(['mt','wa','or','id','nv','ut','ca','az'])
    estacoes_teste = {}
    estacoes_teste['kum'] = set(['id','nv','ut'])
    estacoes_teste['kdois'] = set(['wa','id','mt'])
    estacoes_teste['ktres'] = set(['or','nv','ca'])
    estacoes_teste['kquatro'] = set(['nv','ut'])
    estacoes_teste['kcinco'] = set(['ca','az'])
    
    resultado = algoritmo_ganancioso(estados_teste, estacoes_teste)
    assert len(resultado) <= 5
    assert 'kdois' in resultado
    assert 'ktres' in resultado
    assert 'kum' in resultado or 'kquatro' in resultado
    assert 'kcinco' in resultado
    print("✅ test_algoritmo_ganancioso: Todos os testes passaram!")

test_algoritmo_ganancioso()
print(algoritmo_ganancioso(estados,estacoes))

