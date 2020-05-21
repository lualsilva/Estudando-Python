# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela
#a sua porção inteira.

import math
#from math import trunc

num = float(input('Digite um número fracionado: '))
print('O número {} tem a parte Inteira {}.'.format(num, math.trunc(num)))

""" A baixo tem outras maneiras de fazer sem utilizar módulo, porém, o mais
#indicado é utilizar módulos.

# 1ª
#num = float(input('Digite um número fracionado: '))
#print('O número {} tem a parte Inteira {}.'.format(num, int(num)))

# 2ª
#num = float(input('Digite um número: '))
#print('O número {} tem a parte Inteira {:.0f}.'.format(num, num))

"""