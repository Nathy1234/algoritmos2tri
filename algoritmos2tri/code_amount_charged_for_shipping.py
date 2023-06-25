# Você é um empreendedor e decidiu criar uma nova empresa. Por meio de um plano de negócios, verificou a necessidade de se criar uma 
# transportadora que faz a entrega de produtos a partir de vendas online.

# Para calcular o valor a ser cobrando pelo transporte de uma encomenda desde o fornecedor 
# do produto até a casa do cliente é necessário conhecer a distância (em Km) a ser percorrida e também o peso (em Kg) deste produto.

# Sabe-se que os valores cobrados para cada quilômetro percorrido são:

# Até 500 gramas ou menos: R$ 1,10

# Mais de 500 gramas, mas não mais do que 2 Kg: R$ 2,20

# Mais de 2 Kg, mas não mais de 10 Kg: R$ 3,70

# Mais de 10 Kg: R$ 3,80/Kg mais R$ 1,10 pelo peso que ultrapassar os 10 Kg.

# Implemente um algoritmo que, dados a distância a ser percorrida e o peso da encomenda a ser entregue, calcule e apresente 
# na tela o valor a ser cobrado pelo frete.

distancia = float(input("Digite a distancia percorrida em (km):"))
peso = float(input("Digite o peso da encomenda a ser entregue (kg):"))

if(peso <=0 or distancia <= 0):
    print("O valores invalidos")
    
elif(peso <= 0,5):
    valor_frete = distancia * 1.1
    
elif(peso <= 2):
    valor_frete = distancia * 2.2
    
elif(peso <= 10 ):
    valor_frete = distancia * 3.7

else:
    peso_ultrapassado = peso - 10
    valor_frete = distancia * (3.8  + 1.1 * peso_ultrapassado)

print(f"O valor cobrado pelo frete é R$ {valor_frete:.2f}.")
    