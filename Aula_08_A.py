# -*- coding: utf-8 -*-
# import classe_doce - Importa todas as funcionalidades da biblioteca doce
# import classe_bebidas - Importa todas as funcionalidades da biblioteca bebidas
# from doce import pudim - Impoorta apenas as funcionalidades do pudim da biblioteca doce
# from bebidas import cocacola - Importa apenas as funcionalidades da cocacola da biblioteca bebidas

# math - import math - Importa todas as bobliotecas abaixo
# ceil - Arredonda para cima -
# floor - Arredonda para baixo
# trunc - Truncar da virgula para frente
# pow - Potência
# sqrt - Raiz quadrada - from math import sqrt - Importa apenas os comandos de sqrt da biblioteca math
# factorial - Calculo de fatorial
#
# from math import sqrt,ceil - Importa apenas os comandos de sqrt da biblioteca math

import math
from math import sqrt, floor, ceil

import emoji
from pybovespa.bovespa import *

import urllib3
import sqlalchemy

num = int(input('Digite um número:'))
raiz = math.sqrt(num)
raiz2 = sqrt(num)
print('A raiz de {} é igual a {}'.format(num, math.floor(raiz)))
print('A raiz de {} é igual a {}'.format(num, math.ceil(raiz)))
print('A raiz de {} é igual a {}'.format(num, raiz))

print('A raiz de {} é igual a {}'.format(num, floor(raiz2)))
print('A raiz de {} é igual a {}'.format(num, ceil(raiz2)))
print('A raiz de {} é igual a {}'.format(num, raiz2))

import random

number1 = random.random()
print(number1)

number2 = random.randint(1, 10)
print(number2)

print(emoji.emojize("Olá !! :sunglasses:", use_aliases=True))
print(emoji.emojize("Olá !! :earth_americas: :smile: :stuck_out_tongue_winking_eye: ", use_aliases=True))

# acao = input("Informe o nome da Ação:")
bovespa = Bovespa()
#stock = bovespa.query("PETR3")
#print(stock.cod, stock.name, stock.last, stock.time)


