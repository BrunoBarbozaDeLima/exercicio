def calcular_idade():
    nome = input("Digite seu nome completo: ")

    while True:
        try:
            # Solicita o ano de nascimento e converte para inteiro
            ano_nascimento = int(input("Digite seu ano de nascimento (entre 1922 e 2021): "))

            # Verifica se o ano está dentro do intervalo permitido
            if 1922 <= ano_nascimento <= 2021:
                # Calcula a idade em 2022
                idade = 2022 - ano_nascimento
                print(f"{nome}, você completou ou completará {idade} anos em 2022.")
                break
            else:
                print("Ano inválido. Por favor, insira um ano entre 1922 e 2021.")
        
        # Trata o erro caso o usuário não insira um número válido
        except ValueError:
            print("Entrada inválida. Por favor, insira um número para o ano de nascimento.")

# Executa a função
calcular_idade()
