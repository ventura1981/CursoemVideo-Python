#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
import math
from math import trunc
num = (float(input("Digite um número com casas decimais:")))
inteiro1 = num // 1
inteiro2 = math.trunc(num)
inteiro3 = trunc(num)
inteiro4 = int(num)

resto = num % 1

print("Utilizando divisão inteira: O inteiro deste núro real é {:.2f}".format(inteiro1))
print("Utilizando Math.Trunc: O valor inteiro do número real é {:.2f}".format(inteiro2))
print("Utilizando Trunc: O valor inteiro do número real é {:.2f}".format(inteiro3))
print("Utilizando conversão em inteiro: O valor inteiro do número real é {:.2f}".format(inteiro4))

print("O decimal deste número real é {:.2f}".format(resto))