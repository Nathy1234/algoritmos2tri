# Um valor de média representa um valor médio de uma distribuição. Vários tipos de médias foram inventadas, tais como a média aritmética, 
# média harmônica, média ponderada e média geométrica, entre outras.

# Observe as seguintes fórmulas matemáticas que calculam as médias para cinco valores:

# calculo das medias

# Implemente um algoritmo que solicite ao usuário pelos valores das variáveis a, b, c, d e e. Calcule todas as médias de acordo 
# com as fórmulas acima. Por fim, mostre na tela qual foi a média que apresentou o maior valor das médias calculadas.
# import math

a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
c = int(input("Digite o terceiro valor: "))
d = int(input("Digite o quarto valor: "))
e = int(input("Digite o quinto valor: "))

media_aritmetica = (a + b + c + d + e ) / 4
media_Harmonica = 5 / (1*a + 1*b + 1*c + 1*d + 1*e)
media_ponderada = (1*a + 3*b + 2*c + 3*d + 1*c) / (1+3+2*3*1)
media_geometrica = (a * b * c * d * e) ** (1/5)

maior_media = max(media_aritmetica, media_Harmonica, media_ponderada,media_geometrica)

if(media_aritmetica == maior_media):
    print("A média maior foi: ", media_aritmetica)

elif(media_Harmonica == maior_media):
    print("A maior media foi: ", media_Harmonica)

elif(media_ponderada == maior_media):
    print("A média maior foi: ", media_ponderada)

else:
    print("A média geométrica maior foi: ", media_geometrica)    




