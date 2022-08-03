dia = int(input('A quantos dias o carro foi alugado: '))
km = float(input('Quantos KM o carro percorreu: '))
aluguel = dia*60+km*0.15
print(f'O valor total do aluguel é: {aluguel:.2f}')