"""
1: Crie um algoritmo que seja capaz de apresentar na tela do computador os seus dados pessoais, 
tais como nome completo, cidade em que mora e o nome de seus pais.
"""

"""
while True:  
    nomeCompleto = str(input("Digite o seu nome completo: "))
    if nomeCompleto.isalpha():
        break
    
    else:
        print("Digite um nome valido (somente letras!) ")

    
while True:
    cidade = str(input("Digite a sua cidade: "))
    if cidade.isalpha():
        
        
          break
    else:
        print("Digite uma cidade valida (somente letras): ")
        
      

while True:
    nomeMae = str(input("Digite o nome da sua mãe: "))
    if nomeMae.isalpha():
        
        break

    else:
        print("Digite o nome da mae correto (somente letras): ")
        
        
    
while True:
    nomePai = str(input("Digite o nome do seu pai: "))
    if nomePai.isalpha():
        
          break
        
    else:
        print("Digite o nome do Pai correto (somente letras): ")

"""        
      



"""
# Exercício 02: Indique qual é o tipo de dado para cada valor a seguir:
# a) 2
# b) “Aula de Java”
# c) “p”
# d) 8.6
# e) 0
# f) 0.0
# g) #'x'
# h) True
# i) 789456
# j) -859.4512
# k) “”
# l) ‘ ‘
# m) False

"""
# a) 2 é um número inteiro (int).
# b) “Aula de Java” é uma string (str).
# c) “p” é uma string (str).
# d) 8.6 é um número de ponto flutuante (float).
# e) 0 é um número inteiro (int).
# f) 0.0 é um número de ponto flutuante (float).
# g) #'x' é um símbolo de comentário em Python, não é um valor válido.
# h) True é um valor booleano (bool) que representa verdadeiro.
# i) 789456 é um número inteiro (int).
# j) -859.4512 é um número de ponto flutuante (float).
# k) “” é uma string vazia (str).
# l) ‘ ‘ é uma string que contém um espaço em branco (str).
# m) False é um valor booleano (bool) que representa falso.

"""
Exercício 03: Crie um algoritmo que seja capaz de apresentar na tela o seu nome completo (uma String), a sua 
idade (um número inteiro), a primeira letra do seu nome (um char), a sua altura (um número ponto-flutuante) 
e o sexo (use True para masculino ou False para feminino).

"""


# nomeCpmpleto : "Natalia Araujo de Oliveira"
# idade = 25
# primeiraLetraNome = 'N'
# altura = 1.59
# seuSexo = False

# print("Nome completon\ ", nomeCpmpleto, "" )



"""
Implemente um algoritmo que solicite o nome, a altura, o ano atual e o ano de nascimento de uma pessoa. Em seguida, 
apresente na tela os dados solicitados, a idade atual e a idade em 2050.

"""

# nome = str(input("Qual o seu nome? " ))

# altura = float(input("Qual a sua altura? "))

# anoAtual = int(input("Qual é o ano atual? "))

# anoNascimento = int(input("Digite o ano de nascimento? "))


# idade = anoAtual - anoNascimento

# idade2050 = 2050 - anoNascimento



# print("Nome: ", nome)

# print("Altura: ", altura)

# print("Ano Atual: ")

# print("Ano Nascimento: ", anoNascimento)

# print("A sua idade atual é: ", idade)

# print("Idade em 2050: ", idade2050)

"""
Implemente um algoritmo que solicite o nome de um produto, a quantidade de produtos vendidos e o preço de uma unidade do
produto. Em seguida, apresente um relatório informando o nome do produto, a quantidade vendida, o valor de cada unidade e
calcule o valor total da compra.

"""
# import math


# produto = str(input("Digite o nome de um produto: "))
# quantidadeProduto = int(input("Digite a quantidade de produto vendidos: "))
# precoUnidade = float(input("Digite o preço da unidade do produto: "))

# valorTotal = quantidadeProduto * precoUnidade

# print("O nome do produto é: ", produto)
# print("A quantidade do produto vendido é: ", quantidadeProduto)
# print("O preço unitario do produto vendido é: ", precoUnidade)
# print(f"O valor total foi de: R$ {valorTotal}")


"""O índice de massa corporal (IMC) é uma fórmula matemática utilizada para verificar se uma pessoa adulta está abaixo 
do peso, no peso ideal ou acima do peso. Tem-se que a fórmula é:

O imc é calculado como sendo o peso dividido pela altura ao quadrado

Implemente um algoritmo que solicite ao usuário o seu peso e a sua altura. O algoritmo deve calcular o imc e apresentar o valor obtido.

"""
# import math

# peso = float(input("Digite o seu peso: "))
# altura = float(input("Digite a sua altura: "))

# imc = peso / (altura * altura)

# print(f"O valor obtido foi: {imc :.2f}")

"""
Considere a seguinte situação hipotética: um funcionário de uma empresa recebe um salário base. Sobre este salário, ele possui uma
gratificação de 12% e paga o imposto de 7%. Implemente um algoritmo que solicite ao usuário pelo seu salário base de um funcionário.
O algoritmo deve calcular e apresentar qual será o salário a receber deste funcionário.

"""
# salario = float(input("Digite o seu salário: "))

# gratificação = salario * 0.12
# salario += gratificação

# print("Novo salário: ", salario)

"""
Qual é o resultado da expressão 7 % 4 ?

"""
# expressao = 7 % 4 

# print("Expressão: ", expressao)

"""

Qual é o resultado da expressão 10 // 4 ?

"""

# expressao = 10 // 4

# print(expressao)

"""
Faça um programa contendo uma variável com um número inteiro fornecido pelo usuário e apresente na tela o antecessor e o 
sucessor deste número.
"""

# numInteiro = int(input("Digite um número: "))

# antecessor = numInteiro - 1
# sucessor = numInteiro + 1 

# print("O antecessor é: ",antecessor, "\nO sucessor é: ", sucessor)

"""
Faça um Programa que peça as 4 notas bimestrais e mostre a média aritmética.
"""

# nota1 = int(input("Digite sua nota do primeiro bimestre:"))
# nota2 = int(input("Digite sua nota do primeiro bimestre:"))
# nota3 = int(input("Digite sua nota do primeiro bimestre:"))
# nota4 = int(input("Digite sua nota do primeiro bimestre:"))

# media = (nota1 + nota2 + nota3 + nota4) / 4

# print("A média é: ", media)



"""

Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius.

Celsius é igual a divisão de cinco vezes a subtração do Farenheit e trinta e dois, com o resultado obtido dividido por nove.

"""
# farenheit = float(input("Digite a temperatura farenheit: "))

# celsius = (5*(farenheit - 32)) / 9

# print(f"O resultado obtido foi: {celsius :.2f}")

"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês 
(salário bruto), sabendo-se que são descontados 7.5% para o Imposto de Renda, 8% para o INSS e 1% para o sindicato. Faça um programa que nos dê como resposta:

Seu salário bruto.
Quanto pagou de imposto de renda (calcule sobre o salário bruto).
Quanto pagou ao INSS (calcule sobre o salário bruto).
Quanto pagou ao sindicato (calcule sobre o salário bruto).
O salário líquido (o que sobrou após os descontos).
 

Apresente como saída

+ Salário Bruto: R$

- IR (7.5%): R$

- INSS (8%): R$

- Sindicato (1%): R$

= Salário Líquido: R$

"""



# ganhoHora = float(input("Quanto você ganha por hora: "))
# horasTrabalhadas = float(input("Digite a quantidade de horas trabalhadas: "))

# salarioBruto = 30 * (ganhoHora * horasTrabalhadas)

# impostoRenda = salarioBruto - 7.5
# impostoInss = salarioBruto - 0.8
# sindicato = salarioBruto - 0.1
# salarioLiquido = salarioBruto - impostoRenda - impostoInss - sindicato

# print("+Salário Bruto: R$ ", salarioBruto)
# print("-IR (7.5%): R$ ",impostoRenda)
# print("-INSS (8%): R$ ", impostoInss)
# print(f"-Salário liquido: R$ {salarioLiquido :.2f}")

"""
A Fórmula de Bhaskara é utilizada para determinar as raízes de uma função de segundo grau por meio de seus coeficientes.

Considere a seguinte fórmula:
Tendo-se as variáveis:

      import math

      a = 1.0

      b = -2.0

      c = -3.0

Qual é a instrução para se atribuir à variável x  o valor da fórmula?
"""

# import math

# a = 1.0
# b =-2.0
# c = -3.0

# x = - b + math.sqrt((b * b ) -4 * a * c) / (2*a)

# print("Resultado, o valor de x é:  ", x)

"""
Os logaritmos podem ser usados em diversas áreas, tais como: Matemática e Economia (ex: cálculos financeiros), Química (ex: cálculos de substâncias), Biologia (ex: crescimento de espécies), Geografia (ex: taxa de crescimento populacional), Medicina (ex: dosagem de medicamentos), Computação (ex: avaliação de algoritmos),  etc. 

Utilizando a biblioteca math, qual seria a instrução para se calcular o logaritmo na base 10 do número 100?

Considere as seguintes variáveis:

a = 100

A variável logaritmo deve ser calculada de forma que logaritmo=log10100
"""

# match.log10(a) 

"""
Elabore um algoritmo que solicite ao usuário por dois números ponto-flutuantes.

Em seguida, o algoritmo deve apresentar na tela:

a) A soma dos dois números arredondado pra cima;

b) A soma dos dois números arredondado para baixo;

c) A raiz quadrada da soma dos dois números;

d) O seno do primeiro número informado.
import math

# solicita ao usuário por dois números ponto-flutuantes
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# realiza as operações solicitadas e apresenta os resultados na tela
soma_cima = math.ceil(num1 + num2)
soma_baixo = math.floor(num1 + num2)
raiz = math.sqrt(num1 + num2)
seno = math.sin(num1)

print("Soma arredondada para cima: ", soma_cima)
print("Soma arredondada para baixo: ", soma_baixo)
print("Raiz quadrada da soma: ", raiz)
print("Seno do primeiro número: ", seno)
"""
# import math

# num1 = float(input("Digite um número: "))
# num2 = float(input("Digite o segudo numero: "))

# praCima = math.ceil(num1 + num2)
# paraBaixo = math.floor(num1 + num2)
# raiz = math.sqrt(num1 + num2)
# seno = math.sin(num1)

# print("A soma dos dois numeros arredondados para cima é: ", praCima)
# print("A soma dos dois numeros arredondados para baixo é: ", paraBaixo)
# print("A raiz quadrada da soma é: ", raiz)
# print("O sebo do primero número é: ", seno)


"""
Elabore um algoritmo que seja capaz de sortear quatro números aleatórios.

O primeiro número deve estar entre 0 e 50, inclusos.

O segundo número deve estar entre 10 e 20, inclusos.

O terceiro número deve estar entre 100 e 150, inclusos.

O quarto número deve estar entre 7 e 9, inclusos.

Apresente os quatro números sorteados ao usuário.
"""

# import random

# num1 = random.randint(0,50)
# num2 = random.randint(10,20)
# num3 = random.randint(100,150)
# num4 = random.randint(7,9)

# print("Os numero sorteados foram: ", num1, num2, num3, num4)

"""
A padaria Hotpão vende uma certa quantidade de pães franceses e uma quantidade de broas a cada dia.
Cada pãozinho custa R$ 0,26 e a broa custa R$ 4,50. Ao final do dia, o dono quer saber quanto arrecadou com a venda dos pães e broas 
(juntos), e quanto deve guardar numa conta de poupança (10% do total arrecadado). 

Você foi contratado para fazer os cálculos para o dono. Com base nestes fatos, faça um algoritmo para ler as quantidades
de pães e de broas, e depois calcular e apresentar os dados solicitados.
"""

# paes = 0.26
# broa = 4.50

# quantidadePaes = int(input("Digite a quantidade de paes vendidos: "))
# quantidadeBroas = int(input("Digite a quantidade de broas: "))

# totalVendas = quantidadePaes * paes + (quantidadeBroas * broa)
# poupanca = totalVendas / 10  

# print("A quantidade de paes vendidos foi de: ", quantidadePaes)
# print("A quantidade de broas vendidas foi de: ", quantidadeBroas)
# print("A quantidade total de venda dos dois foram: ", totalVendas)
# print(f"O valor a ser guardado de 10% das vendas foi: {poupanca :.2f}")

"""
A Fórmula de Bhaskara é utilizada para determinar as raízes de uma função de segundo grau por meio de seus coeficientes.

Considere a seguinte fórmula:

menos b mais a raiz quadrada da expressão b ao quadrado menos quatro vezes a vezes c, dividido pelo denominador dois vezes a

Tendo-se as variáveis:

      import math

      a = 1.0

      b = -2.0

      c = -3.0

Qual é a instrução para se atribuir à variável x  o valor da fórmula?

"""
import math

# a = 1.0
# b = -2.0
# c = -3.0

# x = (-b + math.sqrt(b ** 2 - 4 * a * c )) / (2 * a)

# print("A instrução é: ", x)

"""
Uma fábrica controla o tempo de trabalho sem acidentes pela quantidade de dias. Faça um algoritmo para 
converter este tempo em anos, meses e dias. Assuma que cada mês possui sempre 30 dias.

O algoritmo deve solicitar ao usuário pela quantia de dias sem acidente e exibir a conversão em anos, meses e dias.
"""

# dias = int(input("Digite a quantidade de dias sem acidente: "))

# anos = dias // 365
# diasRestantes = dias % 365
# meses = diasRestantes // 30
# diasFinais = diasRestantes % 30


# print(f"{dias} dias correspondem a {anos} anos, {meses} meses e {diasFinais} dias.")

"""
Escreva um algoritmo que solicite dois valores ao usuário: o valor da variável A e o valor da variável B.

O algoritmo deve exibir os valores informados pelo usuário.

Em seguida, o algoritmo deve trocar os valores destas variáveis, fazendo com que a variável A tenha o mesmo valor da variável B, e fazendo com que a variável B tenha o
mesmo valor da variável A.

Apresente novamente os valores das variáveis ao usuário.
"""

# A = int(input("Digite o primeiro valor: "))
# B = int(input("Digite o segundo valor: "))

# C = A
# A = B
# B = C

# print("\nO valor de A é: ",A,"\nO valor de B é: ",B)

"""
Elabore um algoritmo que solicite a hora atual ao usuário. A hora deve ser informada no formato hhmmss (horas minutos e segundos juntos, sendo dois dígitos 
para cada valor).

Por exemplo: 091241 indica que são 9 horas, 12 minutos e 41 segundos.

O algoritmo deve exibir na tela qual é a hora atual, o minuto atual e o segundo atual, cada valor separado por : (dois pontos).

Por exemplo: 9:12:41

DICA: cálculos matemáticos com os números (em especial divisão, multiplicação e subtração).
"""
# import math

# hora = int(input("Digite a hora atual: "))
# minuto = int(input("Digite os minutos: "))
# segundos = int(input("Digite os segundos: "))

# print(f"A hora atual é {hora}:{minuto}:{segundos}")


