# O mesmo professor do desafio anterior quer sortear a ordem de apresentação
#de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos
#e mostre a ordem sorteada.


#import random
from random import shuffle

n1 = input('Digite o nome do 1º aluno: ')
n2 = input('Digite o nome do 2º aluno: ')
n3 = input('Digite o nome do 3º aluno: ')
n4 = input('Digite o nome do 3º aluno: ')
lista = [n1, n2, n3, n4]

#random.shuffle(lista)

shuffle(lista)
print('A ordem de apresentação ficou assim: ')
print(lista)




