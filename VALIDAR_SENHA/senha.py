def validar_senha(senha):

    # Regra 1: Minimo de 8 caracteres

    if len(senha) < 8:
        return False
    
    # a Regra 2: Não pode ser a senha proibida

    if senha == "12345678":
        return False
    
    return True