#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
#  Calcule e mostre o comprimento da hipotenusa.
import math
from math import hypot
cat_adjacente = float(input("Informe o valor do cateto adjacente:"))
cat_oposto = float(input("Informe o valor do cateto oposto:"))

cat_adjacente1 = cat_adjacente ** 2
cat_oposto1 = cat_oposto ** 2

hipotenusa1 = (cat_adjacente1 + cat_oposto1) ** (1/2)
hipotenusa2 = math.hypot(cat_adjacente, cat_oposto)
hipotenusa3 = hypot(cat_adjacente, cat_oposto)

#hipotenusa1 = math.sqrt(cat_adjacente1+cat_oposto1)



print("Utilizando calculos matemáticos: O valor da hipotenusa á {:.2f}".format(hipotenusa1))
print("Utilizando math.hypot: O valor da hipotenusa é {:.2f}".format(hipotenusa2))
print("Utilizando o hypot: O valor da hipotenusa é: {:.2f}".format(hipotenusa3))