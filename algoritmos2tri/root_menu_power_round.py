# Implemente um algoritmo que exiba o seguinte menu de opções:

# MENU:

# 1. Calcular a soma da raízes quadradas de dois números 

# 2. Apresentar na tela uma tabela de potências de 0 a 10

# 3. Arredondar número para cima

# 4. Sair

# OPÇÃO: ____



# Caso o usuário informe a opção 1, o algoritmo deverá solicitar ao usuário por dois valores e exibir na 
# tela a soma das raizes quadradas destes números (ex: (√a)+(√b)
#  )

# Caso o usuário informe a opção 2, o algoritmo deverá solicitar ao usuário por um número e exibir
# na tela uma tabela contendo a potência deste número para os expoentes de 0 a 10 
# (ex:  x0, x1, x2, x3, ..., x10)

# Caso o usuário informe a opção 3, o algoritmo deverá solicitar um número ao usuário e apresentar na 
# tela este número arredondado para cima  (ex: para o número 3.12, o valor arredondado será 4)

# Caso o usuário informe a opção 4, o algoritmo deve ser finalizado.

# Para qualquer opção diferente informada, o algoritmo deve emitir uma mensagem dizendo que a opção é
# inválida.

# Após a execução da opção escolhida, o menu deve ser exibido novamente e uma nova opção deve ser
# informada pelo usuário. O algoritmo só deverá ser finalizado quando o usuário informar a opção correta
# para sair.
import math
opcao = 0

while(opcao != 4):
    print("Calcular a soma da raízes quadradas de dois números\n1. Apresentar na tela uma tabela de potências de 0 a 10\n3. Arredondar número para cima\n4. Sair\n")
    opcao = int(input("OPÇÃO: "))
    
    if(opcao == 1):
        numero1 = int(input("Digite o primeiro número: "))
        numero2 = int(input("Digite o segundo número: "))
        soma = math.sqrt(numero1) + math.sqrt(numero2)
        print(f"A soma das raízes é: {soma:.2f}")


    elif(opcao == 2):
        numero = int(input("Digite o primeiro número: "))
    
        for i in range(1,11):
            print(f"{numero}^{i} = ", numero ** i)
            
    elif(opcao == 3):
        num = float(input("Digite um número: "))
        arrendondar = math.ceil(num)
        print("O número arredondado é: ", arrendondar)
        
    else:
        print("Opção invalida\n")

