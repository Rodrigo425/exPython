num = int(input('Digite um número de quatro digitos: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'Unidade:{u}')
print(f'Dezena:{d}')
print(f'centena:{c}')
print(f'Milhar:{m}')