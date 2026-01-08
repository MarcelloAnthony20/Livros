estados = set(['mt','wa','or','id','nv','ut','ca','az'])
estacoes = {}
estacoes['kum'] = set(['id','nv','ut'])
estacoes['kdois'] = set(['wa','id','mt'])
estacoes['ktres'] = set(['or','nv','ca'])
estacoes['kquatro'] = set(['nv','ut'])
estacoes['kcinco'] = set(['ca','az'])


def algoritmo_ganancioso(estados,estacoes):
    '''
    Essa é uma implementação do algoritmo guloso de conjuntos

    Parâmetros:

    Retorna:
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

print(algoritmo_ganancioso(estados,estacoes))

