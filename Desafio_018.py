#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
angulo = float(input("Informe o valor do ângulo:"))

cos = math.cos(math.radians(angulo))
sen = math.sin(math.radians(angulo))
tan = math.tan(math.radians(angulo))

#print("O ângulo de {1} tem o SENO de {}.\nO ângulo de {1} tem o COSSENO de {}.\nO ângulo de {1} tem a TANGENTE de {}".format(angulo, sen, cos, tan))
print("O ângulo de {} tem o SENO de {:.2f}".format(angulo, sen))
print("O ângulo de {} tem o COSSENO de {:.2f}".format(angulo, cos))
print("O ângulo de {} tem a TANGENTE de {:.2f}".format(angulo, tan))