# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
#e todas as informações possiveis sobre ele.

n = input('Digite algo: ')

print('É do tipo primitivo: {}'.format(type(n)))

print('É alfabético? {}'.format(n.isalpha()))

print('É número inteiro? {}'.format(n.isnumeric()))

print('É espaço? {}'.format(n.isspace()))

print('É alplanumérico? {}'.format(n.isalnum()))

print('Está todo em minúsculo? {}'.format(n.islower()))

print('Está todo em maiúsculo? {}'.format(n.isupper()))

print('Está capitalizada? {}'.format(n.istitle()))

