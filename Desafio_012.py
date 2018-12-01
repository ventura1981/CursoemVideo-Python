# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

precooriginal = float(input('Informe o valor da compra:'))
desconto = float(input('Informe o falor do desconto:'))

resultado = (desconto / 100) * precooriginal

print('Valor do produto: {:.2f}, valor do desconto: {:.2f}, valor final:{:.2f}'.format(precooriginal, resultado, precooriginal - resultado))

