# Escreva um algoritmo que receba uma determinada hora do dia no formato hhmm (ex: 0952 que indica que são 09:52). O algoritmo 
# deve informar se neste horário é de:

# - madrugada, caso a hora esteja entre 00 e 06 horas

# - manhã, caso a hora esteja entre 07 e 12 horas

# - tarde, caso a hora esteja entre 13 e 18 horas

# # - noite, caso a hora esteja entre 19 e 23 horas.


# atual= int(input("Digite a hora do dia em HHMM: "))

minuto = (atual % 100) #Nesta linha, a variável minuto recebe o resto da divisão inteira de atual por 100, ou seja, apenas os dois últimos dígitos querepresentam os minutos.scss 
hora_do_dia = int(atual / 100) 

print("Hora: {:02d}:{:02d}".format(hora_do_dia, minuto))

if(hora_do_dia >= 0 and hora_do_dia <= 6):
    print("Madrugada")

elif(hora_do_dia >= 7 and hora_do_dia <= 12):
    print("Manhã")

elif(hora_do_dia >= 13 and hora_do_dia <= 18):
    print("Tarde")
    
else:
    print("Noite")











# hour = str(input("Digite a hora em formato hhmm: "))

# hour = int(hour[:2])
# print(hour)

# if(hour >= 0 and hour < 6):
#     print("Madrugada")

# elif(hour >= 6 and hour < 12):
#     print("Manhã")

# elif(hour >= 12 and hour < 18):
#     print("Tarde")

# else:
#     print("Noite")
    
