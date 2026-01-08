def programacao_dinamica(str1: str, str2: str) -> int:
    '''
    Calcula o tamanho da maior subsequência comum
    entre duas strings usando programação dinâmica.
    
    Parâmetros:
        str1 (str): Primeira string.
        str2 (str): Segunda string.
    
    Retorna:
        int: Tamanho da maior subsequência comum.
    '''
    tamanho_str1 = len(str1)
    tamanho_str2 = len(str2)
    celula = [[0] * (tamanho_str2 + 1) for _ in range(tamanho_str1 + 1)]
    
    for i in range(1, tamanho_str1 + 1):
        for j in range(1, tamanho_str2 + 1):
            if str1[i - 1] == str2[j - 1]:
                celula[i][j] = celula[i - 1][j - 1] + 1
            else:
                celula[i][j] = max(celula[i - 1][j], celula[i][j - 1])
    
    return celula[tamanho_str1][tamanho_str2]


def test_programacao_dinamica():
    assert programacao_dinamica("fish", "fosh") == 3
    assert programacao_dinamica("fort", "fosh") == 2
    assert programacao_dinamica("abc", "def") == 0
    assert programacao_dinamica("abcdef", "abc") == 3
    assert programacao_dinamica("hish", "vista") == 2
    print("✅ test_programacao_dinamica: Todos os testes passaram!")


test_programacao_dinamica()
