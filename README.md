# exercicio
 Programa que recebe do usuário nome completo e ano de nascimento que seja entre 1922 e 2021. A partir dessas informações, o sistema mostrará o nome do usuário e a idade que completou, ou completará, no ano atual (2022).  Caso o usuário não digite um número ou apareça um inválido no campo do ano, o sistema informará o erro e continuará perguntando até que um valor correto seja preenchido.

# Programa de Cálculo de Idade

Este programa solicita ao usuário que informe seu nome completo e ano de nascimento (entre 1922 e 2021). A partir desses dados, ele calcula e exibe a idade que o usuário completou ou completará em 2022. O programa inclui validação para garantir que o ano inserido esteja no intervalo permitido e que seja um número válido.

## Como funciona o programa

1. O programa solicita ao usuário que digite seu nome completo e armazena essa informação.
2. Em seguida, o programa entra em um loop, solicitando o ano de nascimento do usuário.
3. Dentro do loop:
   - O programa tenta converter o valor digitado para um número inteiro.
   - Se o valor inserido não for um número ou estiver fora do intervalo de 1922 a 2021, uma mensagem de erro é exibida, e o usuário é solicitado a inserir o ano novamente.
4. Caso o valor inserido seja válido, o programa calcula a idade do usuário com base no ano de 2022 e exibe o resultado.
5. O programa então é encerrado.

## Estrutura do Código

```python
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
