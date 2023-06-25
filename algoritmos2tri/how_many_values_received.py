# Crie um algoritmo que solicite ao usuário por um número que representa quantos valores serão fornecidos ao programa.
# Em seguida, leia os n números e apresente, para cada número, o seu triplo. Exemplo:


# Quantos números: 3
# Número: 8 Triplo: 24
# Número: 10 Triplo: 30
# Número: 1 Triplo: 3


num = int(input("Digite quantos valores serão fornececidos: "))

for i in range(num):
    valor = int(input(""))
    triplo = num * 3 
    print("Número: ",num, "Triplo:", triplo)