# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do
#seno, cosseno e tangente dess ângulo.

from math import radians, sin, cos, tan

ângulo = float(input('Digite o ãngulo que você deseja: '))
seno = sin(radians(ângulo))
print('O ãngulo de {} tem o seno de {:.2f}'.format(ângulo, seno))
cosseno = cos(radians(ângulo))
print('O ãngulo de {} tem o cosseno de {:.2f}'.format(ângulo, cosseno))
tangente = tan(radians(ângulo))
print('O ângulo de {} tem a tangente de {:.2f}'.format(ângulo, tangente))
