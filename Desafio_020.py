# O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random
aluno1 = str(input("Informe o nome do primeiro aluno:"))
aluno2 = str(input("Informe o nome do segundo aluno:"))
aluno3 = str(input("Informe o nome do terceiro aluno:"))
aluno4 = str(input("Informe o nome do quarto aluno:"))

lista = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(lista)
print("A sequencia de apresentação será: {}".format(lista))
