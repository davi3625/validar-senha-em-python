from senha import validar_senha

def test_validar_senha_sucesso():
    senha_teste = "SenhaForte2026"
    resultado = validar_senha(senha_teste)
    assert resultado is True, "Deveria aceitar uma senha forte com mais de 8 caracteres"
    print("Teste Senha Forte:  Passou!")

def test_validar_senha_curta():
    senha_curta = "123"
    resultado = validar_senha(senha_curta)
    assert resultado is False, "Não deveria aceitar senha  com menos de 8 caracteres"
    print("Teste Senha Curta: Passou (Bloqueou corretamente)")


def test_validar_senha_proibida():
    senha_comum = "12345678"
    resultado = validar_senha(senha_comum)
    assert resultado is False, "Não deveria aceitar a senha sequencial proibida"
    print("Teste Senha Proibida: Passou (Bloqueou corretamente)")

# Execução dos Testes


if __name__== "__main__":
    print("\n--- Iniciando Testes de Avaliação  ----")
    try:
        test_validar_senha_sucesso()
        test_validar_senha_curta()
        test_validar_senha_proibida()
        print(" --- Todos os Testes foram concluidos com sucesso \n")
    except AssertionError as erro:
        print(f"Falha no teste:  {erro}")



