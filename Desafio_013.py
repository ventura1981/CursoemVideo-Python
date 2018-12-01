# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = float(input('Informe o valor do salário:'))
percentual = float(input('Informe o percentual de aumento:'))

resultado = (percentual / 100) * salario

print('Valor do salario original: {:.2f}, valor do aumento: {:.2f}, valor do salario atualizado: {:.2f}'.format(salario, resultado, salario+resultado))