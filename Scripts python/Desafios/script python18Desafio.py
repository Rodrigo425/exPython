from math import radians, sin, cos, tan
angu = float(input('Digite o angulo: '))
seno = sin(radians(angu))
cosseno = cos(radians(angu))
tangente = tan(radians(angu))
print(f'O angulo é {angu} e tem o seno: {seno:.2f}  \n o cosseno tem {cosseno:.2f} \n e a tangente {tangente:.2f}')
