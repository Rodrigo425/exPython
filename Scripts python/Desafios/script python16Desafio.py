from math import trunc
num = float(input('Digite um número real: '))
numint = trunc(num)
print(f'O número digitado foi {num} e sua porção inteira é {numint}') #A o inves de usar trunc poderia ser int(numint)
