# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
#de um triângulo, calcule e mostre o comprimento da hipotenusa.

from math import hypot
#import math

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adijacente: '))

# Usando "from math import hypot
hi = hypot(co, ca)

# Usando "import math"
#hi = math.hypot(co, ca)

print('A hipotebusa vai medir {:.2f}'.format(hi))


# maneira matematica tradicional
#hi = (co ** 2 + ca ** 2) ** (1/2)
#print('A hipotebusa vai medir {:.2f}'.format(hi))
