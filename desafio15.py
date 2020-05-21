# Escreva um programa que pergunte a quantidade de Km percorridos por um carro
#alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a
#pagar, sabendoque o carro custa R$ por dia e R$0,15 por Km rodado.

km = float(input('Informe a quantidade de Km rodados: '))
dia = float(input('Informe quantos dias de locação: '))
pago = (km * 0.15) + (dia * 60.00)

print('Calculando R${:.2f} por dia + R${:.2f} por km, '
      'o preço total é R${:.2f}'.format(60.00, 0.15, pago))




