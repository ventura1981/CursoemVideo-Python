#Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
#Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
import random
aluno1 = input("Informe o nome do primeiro aluno:")
aluno2 = input("Informe o nome do segundo aluno:")
aluno3 = input("Informe o nome do terceiro aluno:")
aluno4 = input("Informe o nome do quarto aluno:")

lista = [aluno1, aluno2, aluno3, aluno4]
escolhido = random.choice(lista)
print("O aluno escolhido foi: {}".format(escolhido))
