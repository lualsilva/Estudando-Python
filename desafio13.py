# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo
#salário, com 15% de aumento.

salário = float(input('informe o salário do funcionário: R$ '))
novosl = salário + (salário * 15 / 100)
print('O salário do funcionário era R${:.2f}, com o aumento de 15% passou para R${:.2f}'.format(salário, novosl))

