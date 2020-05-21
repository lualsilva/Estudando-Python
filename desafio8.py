# Crie um programa que leia um valor em metros
#e o exiba convertido em centimetros e milimetros...

medida = float(input('Digite a distância em metros: '))
dm = medida * 10
cm = medida * 100
mm = medida * 1000
dam = medida * 0.1
hm = medida * 0.01
km = medida * 0.001
print('A distância de {}m corresponde:\n1- {}km\n2- {}hm\n'
      '3- {:.1f}dam\n4- {:.0f}dm\n5- {:.0f}cm\n6- {:.0f}mm'.format(medida, km, hm, dam, dm, cm, mm))
