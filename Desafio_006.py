# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada

valor = float(input('Digite um valor:'))

dobro = valor * 2
triplo = valor * 3
raiz = valor ** (1/2)

print('Valor digitado: {} \nDobro do valor digitado: {} \nTriplo do valor digitado: {} \nRaiz Quadrada do valor digitado: {:.2f}'.format(valor, dobro, triplo, raiz))
print('Valor digitado: {} \nDobro do valor digitado: {} \nTriplo do valor digitado: {} \nRaiz Quadrada do valor digitado: {:.2f}'.format(valor, valor*2, valor*3, valor**(1/2)))

