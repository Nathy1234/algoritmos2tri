# Você decide abrir uma nova empresa, a MyGame Commerce. Sua loja é especializada na venda de jogos de computadores e 
# video-games e trabalha com diversas plataformas de jogos.

# Você identificou que seus preços são um pouco maiores do que os da concorrência. Entretanto, você decidiu fornecer descontos 
# consideráveis aos clientes caso eles decidam adquirir vários jogos na mesma compra. Para isso, sabe-se:

# Vender de 3 a 5 jogos: desconto de 20%

# Vender de 6 a 8 jogos: desconto de 40%

# Vender mais de 8 jogos: desconto de 50%

# Implemente um software para sua empresa que consiga calcular e mostrar na tela o valor total do desconto e o valor cobrado do
# cliente, considerando os descontos acima descritos. Para a execução do seu algoritmo, será necessário fornecer a quantia de jogos
# que o cliente está comprando e o valor total do preço da compra.

quantia_jogos = int(input("Digite a quantidade de jogos: "))
total = float(input("Preço totoal: "))

if(quantia_jogos >= 3 or quantia_jogos <=5):
    desconto = total * 0.2
    
elif(quantia_jogos >=6 or quantia_jogos <= 8):
    desconto = total * 0.4

elif(quantia_jogos >= 8):
    desconto = total * 0.8

else:
    desconto = 0.0

valor_cobrado = total - desconto

print(f"O valor total de desconto é {desconto:.2f}")
print(f"O valor cobrado com o desconto foi de R$ {valor_cobrado:.2f}")