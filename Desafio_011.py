# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua àrea e a quantidade de tinta necessária para
# pinta-lá, sabendo que cada litro de tinta, pinta uma área de 2m quadrado.

alturaparede = float(input('Informe a altura da parede:'))
larguraparede = float(input('Informe a largura da parede:'))

areaparede = alturaparede * larguraparede

coberturalatatinta = 2

qtdtinta = areaparede / coberturalatatinta

print('Para pintar está parede será necessário {} latas de tinta'.format(qtdtinta))