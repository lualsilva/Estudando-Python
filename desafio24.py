# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não
#com o nome "SÃO".

cid = str(input('Em que cidade você nasceu? ')).strip()
print(cid[:3].upper() == 'SÃO')

