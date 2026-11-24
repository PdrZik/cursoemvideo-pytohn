#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m(2).

n1 = float(input('Digite a largura da parede em metros: '))
n2 = float(input('Digite a altura da parede em metros: '))
area = n1*n2

print('A área total da parede é de {}m(2) e a quantidade de tinta necessária para pintá-la em litros é {}L'.format(area, area/2))