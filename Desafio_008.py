# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.
valor1 = float(input('Insira o valor da metragem linear:'))

valor1emcentimetros = valor1 * 100

valor1emmilimetros = valor1 * 1000

print('O valor inserido é equivalente à {} centimetros.'.format(valor1emcentimetros))
print('O valor inserido é equivalente à {} milimetros.'.format(valor1emmilimetros))