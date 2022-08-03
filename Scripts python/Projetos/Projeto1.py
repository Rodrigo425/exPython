aluno = int(input('Digite quantos alunos tem na sua sala: '))
for cont in range(aluno):
    nome = input('Digite o nome do aluno: ')
    n1 = float(input('Digite a 1º nota do aluno: '))
    n2 = float(input('Digite a 2º nota do aluno: '))
    n3 = float(input('Digite a 3º nota do aluno: '))
    n4 = float(input('Digite a 4º nota do aluno: '))
    soma = n1 + n2 + n3 + n4
    resultado = soma/4
    if resultado >=5:
        print(f'Aprovado média do aluno: {resultado}')
    else:
        print(f'Reprovado média do aluno: {resultado}')
    