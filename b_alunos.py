alunos = []
id_alunos = 1

def cadastro_aluno():

    global id_alunos

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
        "id": id_alunos,
        "nome": nome,
        "idade": idade
    }

    alunos.append(aluno)
    id_alunos += 1

    print('Aluno cadastrado.')
    input('Clique ENTER para continuar...')


def atualizar_alunos():

    nome_b = input(
        'Digite o nome do aluno que você deseja atualizar: '
    )

    for aluno in alunos:

        if aluno['nome'] == nome_b:

            while True:

                nome_novo = input(
                    "Digite o novo nome para cadastro: "
                )

                if nome_novo.replace(' ', '').isalpha():
                    break

                print('Digite somente letras.')

            while True:

                idade_nova = input(
                    'Digite sua nova idade: '
                )

                if idade_nova.isdigit():

                    idade_nova = int(idade_nova)
                    break

                print('Digite somente numeros.')

            aluno['nome'] = nome_novo
            aluno['idade'] = idade_nova

            print('Aluno atualizado com sucesso!')

            return

    print('Aluno não encontrado.')
