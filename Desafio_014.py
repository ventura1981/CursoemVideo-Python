#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit
print("Conversor de Temperatura - Celius em Fahrenheit")
tempcelcius = float(input("Insira a temperatura em Celcius:"))
tempfahrenheit = tempcelcius * 9 / 5 + 32

print("{}º Celcius equivale a {:.2f}º Fahrenheit".format(tempcelcius, tempfahrenheit))