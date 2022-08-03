nome = input('Digite seu nome: ')
print('Prazer em te conhecer: {:=^20}'.format(nome))

print('Prazer em te conhecer: {:^20}'.format(nome))

print('Prazer em te conhecer: {:20}! '.format(nome))

print('Prazer em te conhecer: {:>20}!'.format(nome))

print('Prazer em te conhecer: {:<20}!'.format(nome))

valor1 = int(input('Digite um valor: '))
valor2 = int(input('Digite outro valor: '))

divis = valor1/valor2
#Usar o {:.valorf} serve para selecionar quantos números irão aparecer depois do ponto
# exemplo {:.3f} ira aparecer 3 números depois do ponto
print('O resultado da divisão é: {:.3f}'.format(divis))