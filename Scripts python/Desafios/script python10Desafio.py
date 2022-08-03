real = float(input('Digite quanto dinheiro você tem na carteira? R$ '))
dolar = real/4.18
dolaraustraliano = real/2.88
yen = real/0.038
print(f'Com R${real:.2f} você pode comprar US{dolar:.2f} \n Dolar australiano {dolaraustraliano:.2f} \n Yen  ¥{yen:.2f}')