numero = input('Digite algo: ')
print(numero.isnumeric())
# O comando .isnumeric() informa se o que o usuario digitou é número ou não Exibindo: True para sim, E False para não

# O camando .isalpha() informa se o que o usuario digitou é Letra ou não exibindo: True para sim, E false para não
letra = input('Digite algo: ')
print(letra.isalpha())

# O comando .isalnum() informa se oque o usuario digitou é letra com número ou se e apenas número ou se é apenas letra exibindo: True ou se não for nenhum é False
letranumero = input('Digite algo: ')
print(letranumero.isalnum())

# O comando .isupper() informa se oque o usuario digitou esta so em maiusculo exibindo:True, se estiver em letras minuscula ou em minuscula e maiscula exibe:False
maiorletra = input('Digite algo: ')
print(maiorletra.isupper())

# O comando .islower() informa se oque o usuario digitou esta so em minusculo exibindo:True, se estiver em letras minusculas e maisculas ou apenas em maiscula exibe False
menorletra = input('Digite algo: ')
print(menorletra.islower())

# O comando .isspace() informa se tem espaço exibindo:True agora se não tiver espaço exibe False
espaço = input('Digite algo: ')
print(espaço.isspace())

# O comando .istitle() informa se a primeira letra do que foi digitado é maiuscula exibindo:True se a primeira letra não for maiuscula exibe False
title = input('Digite algo: ')
print(title.istitle())

# Existem muitos comandos .is cada um com alguma função diferente