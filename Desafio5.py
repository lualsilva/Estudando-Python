# Digite um numero e o programa vai mostrar o sucessor e antecessor.

n = int(input('Digite um número: '))

# Utilizando variáveis, utilizado caso eu precisasse dele mais pra frente
#a = n - 1
#s = n + 1
#print('Analisando o valor {}, seu antecessor é {} e o sucessor é {}'.format(n, a, s))


# Utilizado apenas uma variável, pois eu não vou usá-las mais para frente
print('Analisando o valor {}, seu antecessor é {} e o sucessor é {}'.format(n, (n-1), (n+1)))

#Observação os dois jeitos estão certos, vai da necessidade.
