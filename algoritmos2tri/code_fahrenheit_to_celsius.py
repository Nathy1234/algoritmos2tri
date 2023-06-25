# Escreva um algoritmo que faz conversão de temperaturas de Fahrenheit para Celcius, seguindo a fórmula:

# C=59(F−32)

# O usuário deverá informar uma temperatura em graus Fahrenheit (F), o algoritmo deverá calcular a temperatura equivalente em graus C
# elcius (C).

# Em seguida, o algoritmo deverá apresentar as seguintes mensagens, de acordo com as condições estabelecidas:

# "Hoje está bem quente" (para temperaturas acima de 30ºC)

# "Hoje está gostoso" (para temperaturas entre 20ºC e 30ªC)

# "Hoje está frio" (para temperaturas entre 10ºC e 20ºC)

# "Hoje está muito frio" (para temperaturas abaixo de 10ºC)

# f = float("Digite a temperatura em Fahrenheit ºf: ")


f = float(input("Digite a temperatura: "))

c = (5 * (f - 32)) / 9

print("Em celsius", c)

if(c > 30):
    print("Hoje esta bem quente")

elif(c >= 20 and c < 30):
    print("Hoje está gostoso")

elif(c > 10 and c < 20):
    print("hoje esta friu")

else:
    print("Hoje esta muito friu")














# f = float(input("Informe a temperatura em ºF: "))

# c = 5/9 * (f-32)

# print("Em Celcius: ", c)

# if(c > 30):

#     print("Hoje está bem quente")

# elif(c >=20 and c <= 30):

#     print("Hoje está gostoso")

# elif(c >= 10 and c < 20):

#     print("Hoje está frio")

# else:

#     print("Hoje está muito frio")