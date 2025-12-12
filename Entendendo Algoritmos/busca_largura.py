from collections import deque

def busca_largura(grafo:dict, raiz:str, alvo:str)->bool:
    '''
    Realiza uma busca em largura para verificar se existe caminho entre raiz e alvo.

    Parâmetros:
        grafo (dict): Um dicionário representando o grafo onde as chaves são nós 
                      e os valores são listas de nós adjacentes.
        raiz (str): O nó inicial da busca.
        alvo (str): O nó que se deseja encontrar.

    Retorna:
        bool: True se houver caminho da raiz até o alvo, False caso contrário.
    '''
    fila_de_pesquisa = deque()
    fila_de_pesquisa += grafo[raiz]
    verificados = []
    
    while fila_de_pesquisa:
        item = fila_de_pesquisa.popleft()
        if item not in verificados:
            if item == alvo:
                return True
            else:
                fila_de_pesquisa += grafo[item]
                verificados.append(item)
    return False

def test_busca_largura():
    grafo = {
        'voce': ['alice', 'bob', 'claire'],
        'alice': ['peggy'],
        'bob': ['anuj', 'peggy'],
        'claire': ['thom', 'jonny'],
        'anuj': [],
        'peggy': [],
        'thom': [],
        'jonny': []
    }
    assert busca_largura(grafo, 'voce', 'anuj') == True
    assert busca_largura(grafo, 'voce', 'peggy') == True
    assert busca_largura(grafo, 'alice', 'thom') == False
    print("✅ busca_largura: Todos os testes passaram!")

test_busca_largura()

grafo = {}