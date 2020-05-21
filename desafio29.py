# Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$7,00 por cada Km acima do limite.

vel = float(input('Informa a velocidade do carro Km/h: '))
if vel > 80:
    print('"MULTADO". Velocidade máxima de 80Km/h excedida em {}Km/h'.format(vel-80))
    print('Será multado R$7,00 por Km/h excedente, totalizando R${}'.format(7*(vel-80)))
print('Digija com segurança e boa viagem!')
