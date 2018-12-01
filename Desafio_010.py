# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
# Considere U$$1,00 = R$3,27

carteira = float(input('Quantos Reais você tem na carteira?'))
precodollaremreais = 3.27
podecomprar = carteira / precodollaremreais

print('Com está quantia você pode trocar por {:.2f} dólares.'.format(podecomprar))