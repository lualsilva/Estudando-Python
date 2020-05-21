# Crie um programa que leia um valor e mostre o seu dobro, triplo
#e raiz quadrada

v = int(input('Digite um valor: '))
#d = v * 2
#t = v * 3
#r = v ** (1/2)
print('O valor digitado foi: {}.'.format(v))
#print('O dobro é: {}.\nO triplo é: {}.\nA raiz quadra é: {:.2f}.'.format(d, t, r))

# Outra forma de fazer:
print('O dobro é: {}.\nO triplo é: {}.\nA raiz quadra é: {:.2f}.'.format((v*2), (v*3), (v**(1/2))))


