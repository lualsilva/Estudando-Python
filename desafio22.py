""""
# Crie um programa que leia o nome completo de uma pessoa e mostre:
# 1-O nome com todas as letras maiúsculas.
# 2-O nome com todas as letras minúsculas.
# 3-Quantas letras ao todo (sem considerar espaços).
# 4-Quantos letras tem o primeiro nome.

"""

nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculo é {}'.format(nome.upper()))
print('Seu nome em minúsculo é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
# ou
separa = nome.split()
print('Seu primeiro nome é {} e tem {} letras'.format(separa[0], len(separa[0])))




