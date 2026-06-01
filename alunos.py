alunos = []

def cadastro_aluno():
    
    while True:
        nome = input("Digite o seu nome para o cadastro: ")
        if nome.replace('','').isalpha():
            break

        print('Digite somente letras.')

cadastro_aluno()