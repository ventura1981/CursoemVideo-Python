# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e antecessor.

valor = int(input('Digite um número inteiro:'))
#sucessor = valor + 1
#antecessor = valor -1

#print('{:=20}')
print('Valor digitado: {:>10} \nSucessor: {:>10} \nAntecessor: {:>10}'.format(valor, valor+1, valor-1))