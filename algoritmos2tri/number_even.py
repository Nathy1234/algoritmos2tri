# Elabore um algoritmo que solicite números ao usuário até que ele digite o número zero. Quando o programa terminar, apresente na tela quantos
# números pares entre 1 e 50 foram digitados. Utilize o laço de repetição while. Exemplo:

# Digite um número: 200
# Digite um número: 62
# Digite um número: 30
# Digite um número: 11
# Digite um número: 9
# Digite um número: 10
# Digite um número: 0
# Quantidade de números pares entre 1 e 50: 2

cont = 0 
num = int(input("Digite um número: "))

while num != 0:
    if(num % 2 == 0 and num >= 1 and num <= 50):
        cont += 1
    num = int(input("Digite um número: "))
    
print("Quantidade de números pares entre 1 e 50: ", cont)