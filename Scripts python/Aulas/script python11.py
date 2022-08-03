# Aula #09

frase = 'Pycharm'
print(frase[1]) # Comando serve dizer apartir de qual letra começa a frase

frase2 = 'Pycharm'
print(frase2[1:8]) # O comando serve para dizer aonde frase começa e onde termina

frase3 = 'Pycharm'
print(frase3[:6]) # Este comando serve não mostra onde começa então ira começar do começo ate onde colocou para terminar a frase

frase4 = 'Pycharm' # Este comando mostra aonde começa e não mostra onde termina a frase então ira ate o final
print(frase4[0:])

frase5 = 'Pycharm'
print(frase5[2:7:2]) # Este comando mostra onde começã e onde termina e quantos números ira pular de letra em letra na frase 

frase6 = 'Pycharm'
print(frase6[1::2]) # Este comando mostra onde começa não mostra onde termina então ira ate o final frase pulando de letra em letra

frase7 = 'Pycharm'
print(frase7[::2]) # Este comando não mostra aonde começa e não mostra aonde termina mostra apenas quanto ira pular de letra a letra

print("""Python é uma linguagem de programação de alto nível,[4] interpretada, de script, imperativa,
orientada a objetos, funcional, de tipagem dinâmica e forte. Foi lançada por Guido van Rossum em 1991.
[1] Atualmente possui um modelo de desenvolvimento comunitário, aberto e gerenciado pela organização sem 
fins lucrativos Python Software Foundation. Apesar de várias partes da linguagem possuírem padrões e 
especificações formais, a linguagem como um todo não é formalmente especificada. O padrão de facto é a 
implementação CPython.

A linguagem foi projetada com a filosofia de enfatizar a importância do esforço do programador sobre o 
esforço computacional. Prioriza a legibilidade do código sobre a velocidade ou expressividade. 

Combina uma sintaxe concisa e clara com os recursos poderosos de sua biblioteca padrão e por módulos e
frameworks desenvolvidos por terceiros.

Python é uma linguagem de propósito geral de alto nível, multiparadigma, suporta o paradigma orientado a objetos,
imperativo, funcional e procedural. Possui tipagem dinâmica e uma de suas principais características é permitir
a fácil leitura do código e exigir poucas linhas de código se comparado ao mesmo programa em outras linguagens.

Devido às suas características, ela é principalmente utilizada para processamento de textos, 
dados científicos e criação de CGIs para páginas dinâmicas para a web. Foi considerada pelo público a
3ª linguagem "mais amada", de acordo com uma pesquisa conduzida pelo site Stack Overflow em 2018,[5] e 
está entre as 5 linguagens mais populares, de acordo com uma pesquisa conduzida pela RedMonk.""")

# Caso queira escrever um longo texto não é necessario um print para cada linha
# do texto basta colocar print("""O texto""") para que seja exibido o texto inteiro

frase8 = ('o programa de python é o Pycharm') # O comando do .count serve para exibir quantas vezes uma determinada letra minuscula aparece em uma frase 
print(frase8.count('o'))

frase9 = ('O programa de python é o pycharm') # O comando upper().count() serve para exibir quantas vezes uma determinada letra maiuscula aparece em uma frase
print(frase9.upper().count('O'))

frase10 = ('  O programa de python é o pycharm  ') # O comando len() serve para exibir quantas letras tem em uma determinada frase e tambem e contado como caractere o espaço
print(len(frase10))

frase11 = ('  O programa de python é o pycharm  ') #O comando .strip serve para remover os espaço da frase
print(len(frase11.strip()))

frase12 = ('O programa de python é o pycharm')
print(frase12.replace('pycharm', 'visual studio')) # O comando .replace() serve para mudar uma determinada palavra de frase exemplo .replace('palavra da frase', 'palavra que ira substituir')

frase13 = ('O programa de python é o pycharm') # O comando .find procura a palavra na frase e indica a posição caso a palavra não exista ele exibe -1
print(frase13.find('programa'))

frase14 = ('O programa de python é o pycharm') # O comando .lower().find('palavra a ser procurada na frase') procura uma palavra em letra minuscula numa frase
print(frase14.lower().find('programa'))

frase15 = ('O programa de python é o pycharm') # O comando .split() serve para dividir as frases que tem espaço e exibir separadamente como uma lista
print(frase15.split())

frase16 = ('O programa de python é o pycharm') # O comando serve para pegar uma palavra da lista que esta dividida
dividido = frase16.split()
print(dividido[1])

frase17 = ('O programa de python é o pycharm') # O comando serve para pegar uma palavra da lista que esta dividida e exibir uma letra em especifico 
dividido2 = frase17.split()
print(dividido2[1][2])

