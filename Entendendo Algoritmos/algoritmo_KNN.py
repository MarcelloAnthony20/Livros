import math

def distancia_euclidiana(ponto1:tuple, ponto2:tuple) -> float:
    '''
    Calcula a distância euclidiana entre dois pontos.

    Parâmetros:
        ponto1 (tuple): Coordenadas do primeiro ponto (x, y, ...).
        ponto2 (tuple): Coordenadas do segundo ponto (x, y, ...).

    Retorna:
        float: A distância euclidiana entre os dois pontos.
    '''
    resultado = 0
    for coordenada1, coordenada2 in zip(ponto1, ponto2):
        resultado += (coordenada1 - coordenada2) ** 2
    return math.sqrt(resultado)
        
    
    


def knn(dados_treino, ponto_teste, k):
    '''
    Implementa o algoritmo K-Nearest Neighbors (KNN) para classificação.
    
    O algoritmo encontra os k vizinhos mais próximos de um ponto de teste
    e retorna a classificação mais comum entre esses vizinhos.

    Parâmetros:
        dados_treino (list): Lista de tuplas contendo (coordenadas, classificação).
        ponto_teste (tuple): Coordenadas do ponto a ser classificado.
        k (int): Número de vizinhos mais próximos a considerar.

    Retorna:
        str: A classificação do ponto de teste baseada nos k vizinhos mais próximos.
    '''
    vizinhos = []
    
    for ponto in dados_treino:
        coordenadas, classe = ponto
        dist = distancia_euclidiana(coordenadas, ponto_teste)
        vizinhos.append((dist, classe))
    
    vizinhos.sort()
    classes = [vizinhos[i][1] for i in range(k)]
    return max(set(classes), key=classes.count)    


def test_distancia_euclidiana():
    assert distancia_euclidiana((0, 0), (3, 4)) == 5.0
    assert distancia_euclidiana((1, 1), (1, 1)) == 0.0
    assert distancia_euclidiana((0, 0), (1, 1)) == math.sqrt(2)
    assert round(distancia_euclidiana((2, 3), (5, 7)), 2) == 5.0
    print("✅ test_distancia_euclidiana: Todos os testes passaram!")


def test_knn():
    # Conjunto de dados de exemplo: filmes (comédia/ação)
    dados_treino = [
        ((3, 4), 'comédia'),   # muita comédia, pouca ação
        ((2, 5), 'comédia'),
        ((1, 4), 'comédia'),
        ((5, 1), 'ação'),      # muita ação, pouca comédia
        ((4, 2), 'ação'),
        ((5, 2), 'ação')
    ]
    
    # Teste 1: Ponto próximo de comédias
    assert knn(dados_treino, (2, 4), 3) == 'comédia'
    
    # Teste 2: Ponto próximo de ações
    assert knn(dados_treino, (4, 1), 3) == 'ação'
    
    # Teste 3: Usando k=5
    assert knn(dados_treino, (3, 3), 5) in ['comédia', 'ação']
    
    # Conjunto de dados: frutas (laranja/toranja)
    dados_treino2 = [
        ((150, 7), 'laranja'),
        ((170, 7.5), 'laranja'),
        ((140, 6.8), 'laranja'),
        ((200, 10), 'toranja'),
        ((190, 9.5), 'toranja'),
        ((210, 10.2), 'toranja')
    ]
    
    # Teste 4: Classificação de frutas
    assert knn(dados_treino2, (160, 7.2), 3) == 'laranja'
    assert knn(dados_treino2, (195, 9.8), 3) == 'toranja'
    
    print("✅ test_knn: Todos os testes passaram!")


# Executar os testes
test_distancia_euclidiana()
test_knn()
