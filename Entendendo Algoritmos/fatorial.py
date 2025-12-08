def fatorial(num:int)->int:
    '''
    Calcula o fatorial de um número inteiro de forma recursiva.

    Parâmetros:
        num (int): O número inteiro para o qual o fatorial será calculado.
            Deve ser um número inteiro não negativo.

    Retorna:
        int: O valor do fatorial de `num`.

    Exceções:
        ValueError: Se `num` for negativo.
    '''
    if num < 0:
        raise ValueError('O fatorial não está definido para números negativos.')
    if num <= 1:
        return 1
    return num * fatorial(num - 1)
    
def test_fatorial():
    assert fatorial(5) == 120
    assert fatorial(3) == 6
    assert fatorial(1) == 1
    assert fatorial(0) == 1
    try:
        fatorial(-1)
    except ValueError as e:
        assert str(e) == "O fatorial não está definido para números negativos."
    else:
        assert False, "Era esperado um ValueError para números negativos."
    print("✅ test_fatorial: Todos os testes passaram!")

test_fatorial()
