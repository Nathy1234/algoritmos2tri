# Elabore um algoritmo que solicite números ao usuário até que ele digite o número um. Quando o programa 
# terminar, apresente na tela:

# - a soma dos números pares que foram digitados. 

# - a soma dos números ímpares que foram digitados.

# - o total de números múltiplos de 3 que foram digitados.

# Utilize o laço de repetição while. Exemplo:


# Digite um número: 2
# Digite um número: 6
# Digite um número: 3
# Digite um número: 11
# Digite um número: 9
# Digite um número: 1
# Soma dos pares: 8
# Soma dos ímpares: 24
# Total de múltiplos de 3: 3


soma_pares = 0
soma_impares = 0
total_multiplos3 = 0
num = 0


while(num != 1):
    num = int(input("Digite um número: "))
    if(num % 2 == 0):
        soma_pares += num
    else:
        soma_impares += num
    
    if(num % 3 == 0 ):
        total_multiplos3 += 1   
    
print("Soma dos números pares: ", soma_pares)
print("Soma dos números imapres: ", soma_impares)
print("Total de multiplos de 3: ", total_multiplos3)    

