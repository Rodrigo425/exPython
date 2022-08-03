nome = str(input('Escreva um nome: ')).strip()
letramax = nome.upper()
letramin = nome.lower()
primeironome = nome.split()
print(f'O nome com todas as letras em maiusculo {letramax}\nO nome com todas letras minusculas {letramin}')
print(f'A quantidade de letras do nome {nome} é:', len(nome)-nome.count(' '))
print(f'O primeiro nome {len(primeironome[0])} ')

