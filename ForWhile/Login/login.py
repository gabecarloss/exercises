while True:

    nome = input("Digite seu nome: ")
    if len(nome) < 5:
        print("Nome deve conter pelo menos 5 caracteres. Tente novamente.")
        continue

    while True:
        senha = input("Digite sua senha: ")
        if len(senha) < 8:
            print("Senha deve conter pelo menos 8 caracteres. Tente novamente.")
            continue
        break

    print("Cadastro bem-sucedido!")
    break