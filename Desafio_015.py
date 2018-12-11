#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias
#  pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15
# por Km rodado.
#

print("Sistema de Pagamento Localiza")
data_retirada = float(input("Informe o dia em que o carro foi retirado:"))
data_entrega = float(input("Informe o dia em que o carro foi entregue:"))
kmrodado = float(input("Informe quantos quilometros foram percorridos:"))

valor_aluguel_dias = (data_entrega - data_retirada) * 60
valor_km = kmrodado * 0.15
valor_total = valor_aluguel_dias + valor_km

valor_total2 = (data_entrega - data_retirada) * 60 + kmrodado * 0.15
print("Dias com o carro: {} x R$60,00 = R${:.2f}".format(data_entrega - data_retirada, valor_aluguel_dias))
print("Km percorrido: {} x R$0,15 = R${:.2f}".format(kmrodado,valor_km))
print("O valor do aluguel é R${:.2f}".format(valor_total))
print("O valor do aluguel é R${:.2f}".format(valor_total2))
