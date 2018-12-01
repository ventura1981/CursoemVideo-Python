# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

notaportugues1 = float(input('Digite a nota de Português no primeiro semestre:'))
notaportugues2 = float(input('Digite a nota de Português no segundo semestre:'))

mediaanualportugues = (notaportugues1 + notaportugues2) / 2

print('A média anual de português é {}'.format(mediaanualportugues))