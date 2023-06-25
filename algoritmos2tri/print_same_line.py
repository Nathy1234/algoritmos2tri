# No Python 3.x, cada comando print() é exibido em uma linha, ou seja, existe um 
# “\n” ao final da apresentação do conteúdo na tela. Para que não haja quebra de linha e os comandos 
# print() sejam exibidos na mesma linha, podemos utilizar vários comandos print("mensagem", end=""). 
# Neste sentido, implemente um algoritmo que, com apenas um comando print(“*”, end=“”) apresente os 
# seguintes padrões na tela (caso seja necessário a quebra de linha, utilize print()):

# *********
# ********
# *******
# ******
# *****
# ****
# ***
# **
# *

for i in range(9 , 0 , -1):
    print("*" * i, end= "")
    print