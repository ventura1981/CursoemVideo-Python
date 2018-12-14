#
frase = 'Curso em Video Python'
print(frase)
print(frase[9])         #pega só o caractere 9
print(frase[15])        #pega só o caractere 9
print(frase[9:13])      #pega do 9 ao 12
print(frase[9:21])      #pega do nove ao 20
print(frase[9:21:2])    #pega do 9 ao 21 saltando de dois em dois
print(frase[:5])        #pega do inicio(0) até o caractere 5
print(frase[15:])       #pega do caractere 15 até o final
print(frase[9::3])      #pega do 9 até o final, porem salta de 3 em 3

qtdcaracteres = len(frase)      #conta quantos caracteres a string possui
print(qtdcaracteres)

qtd_o = frase.count('o')        #conta quantas letras 'o' tem na variavel
qtd_o2 = frase.count('o',0,13)  #conta quantas letras 'o' tem entre o caracter 0 e o 13
print(qtd_o)
print(qtd_o2)

pesquisa = frase.find('deo')    #pesquisa se existe o conjunto 'deo' dentro da variavel e informa a posição inicial
print(pesquisa)

pesquisa2 = frase.find('Android')   #retorna o valor -1 informando que não encontrou o conjunto de caracteres
print(pesquisa2)

pesquisa3 = 'Curso' in frase    #restorna True se encontrar o conjunto de caracteres e False caso não encontre
print(pesquisa3)

substituir = frase.replace('Python','Android')  #faz a substituição de um conjunto de caracteres por outro via método
print(substituir)

maiuscula = frase.upper()       #passa todos os caracteres para maiusculo através de método
print(maiuscula)

minusculo = maiuscula.lower()   #passa todos os caracteres para minusculo através de método
print(minusculo)

capitalize = frase.capitalize() #passa todos os caracteres para minusculo e depois coloca apenas o primeiro caractere em maiusculo
print(capitalize)

titulo = frase.title()          #passa tudo para minusculo e depois coloca o primeiro caractere de cada palavra em maiusculo
print(titulo)

