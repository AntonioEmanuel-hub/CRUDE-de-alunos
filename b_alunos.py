alunos = []

def cadastro_aluno():
    
    while True:
        nome = input("Digite o seu nome para o cadastro: ")

        if nome.replace(' ', '').isalpha():
            break

        print('Digite somente letras.')

    while True:
        idade = input('Digite sua idade: ')

        if idade.isdigit():
            idade = int(idade)

            break
        print('Digite somente numeros.')

    aluno ={

        "nome": nome,
        "idade": idade
    }

    alunos.append(aluno)

    print('Aluno cadastrado.')
    input('Clique ENTER para continuar...')