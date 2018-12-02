# -*- coding: utf-8 -*-
# Operadores
# + Adição
# - Subtração
# * Multiplicação
# / Divisão
# ** Potência
# // Divisão Inteira
# % Resto da Divisão
5 + 2 == 7
5 - 2 == 3
5 * 2 == 10
5 / 2 == 2.5
5 ** 2 == 25
5 // 2 == 2
5 % 2 == 1

# Ordem de Precedência
# 1 ()
# 2 **
# 3 * / // %
# 4 + -

5 + 3 * 2 == 11
3 * 5 + 4 ** 2 == 31
3 * (5 + 4) ** 2 == 243

# Calcular a Raiz Quadrada
81**(1/2)
25**(1/2)

# Calcular a Raiz Cubica
127**(1/3)

# Formatação de saida do print
nome=input('Qual é o seu nome?')
print('Prazer em te conhecer {}!'.format(nome))
print('Prazer em te conhecer {:20}!'.format(nome))
print('Prazer em te conhecer {:<20}!'.format(nome))
print('Prazer em te conhecer {:>20}!'.format(nome))
print('Prazer em te conhecer {:^20}!'.format(nome))
print("Prazer em te conhecer {:^20}!".format(nome))

n1 = int(input('Um valor:'))
n2 = int(input('Outro valor:'))
print('A soma vale {}'.format(n1+n2))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, \n o produto é {} e a \n divisão é {:.4f}'.format(s, m, d))
print('Divisão inteira {} e potência {}'.format(di, e))

# \n quebra a linha
# , end=' ') concatena a saida de dois prints