from random import shuffle
a1 = input('Escreva o nome do 1° aluno: ')
a2 = input('Escreva o nome do 2° aluno: ')
a3 = input('Escreva o nome do 3° aluno: ')
a4 = input('Escreva o nome do 4° aluno: ')
lista = [a1, a2, a3, a4]
shuffle(lista)
print(f'A ordem de apresentação dos alunos será \n {lista}')