cidade = str(input('Escreva o nome da sua cidade: ')).split()
cidadfind = cidade.find()
if cidadfind == -1:
    print('O nome da sua cidade não começa com a palavra SANTO')
else:
    print('O nome da sua cidade começa com a palavra SANTO')