from math import hypot
cateopos = float(input('Qual é o comprimento do cateto oposto: '))
cateadja = float(input('Qual é o comprimento do cateto adjacente: '))
hipotenusa = hypot(cateopos, cateadja)
print(f'A hipotenusa vai medir: {hipotenusa:.2f}')