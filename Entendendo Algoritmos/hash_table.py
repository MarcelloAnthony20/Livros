def hash(item: str) -> int:
    '''
    Calcula o índice hash para um item baseado na primeira letra.
    
    Parâmetros:
        item (str): String para calcular o hash.
    
    Retorna:
        int: Índice de 1 a 26 baseado na primeira letra (a=1, b=2, ..., z=26).
    '''
    return ord(item[0].lower()) - ord('a') + 1


def hash_table(item: str, tabela: list) -> None:
    '''
    Insere um item na hash table usando encadeamento para tratar colisões.
    
    Parâmetros:
        item (str): String a ser inserida na tabela.
        tabela (list): Lista representando a hash table (deve ter 26 posições).
    
    Retorna:
        None: A função modifica a tabela diretamente.
    '''
    posicao = hash(item)
    if not tabela[posicao]:
        tabela[posicao] = [item]
    else:
        tabela[posicao].append(item)


def test_hash():
    assert hash("apple") == 1
    assert hash("banana") == 2
    assert hash("zebra") == 26
    assert hash("Apple") == 1
    print("✅ test_hash: Todos os testes passaram!")


def test_hash_table():
    tabela_teste = [None] * 26
    hash_table("apple", tabela_teste)
    assert tabela_teste[1] == ["apple"]
    hash_table("banana", tabela_teste)
    assert tabela_teste[2] == ["banana"]
    hash_table("avocado", tabela_teste)
    assert tabela_teste[1] == ["apple", "avocado"]
    assert tabela_teste[3] is None
    print("✅ test_hash_table: Todos os testes passaram!")


test_hash()
test_hash_table()
