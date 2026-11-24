#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos doláres ela pode comprar.
#Considere:
#U$1.00 = R$3.27

n= float(input('Digite quanto de dinheiro tem na carteira: '))
print('Você pode comprar U${} com isso.'.format(n/3.27))