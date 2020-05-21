# Crie um programa que converta Reais em Dólares, considerando 1 Dólar a R$5.50

real = float(input('Quanto dinheiro você quer converter? R$ '))
dolar = real / 5.50
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))


