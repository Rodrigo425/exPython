salario = float(input('Digite o salario atual do funcionário: R$'))
calculo = salario+(salario*15/100) # <- (salario*15/100) <- porcentagem
print(f'Este é o novo salário do funcionário com aumento de 15%: R${calculo:.2f}')