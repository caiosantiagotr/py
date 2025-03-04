mesdoano = {"janeiro" , "março", "maio"}
dias = set([5, 10, 7, 3, 9])
# 3 removido , 5 removido removido 10 removido 9 
# nesses meses eu quero escolher alguns dias para fazer alguma festa
conjunto1 = {5, 10,3}
# dos dias dos mes que eu quero escolher 
conjunto2 ={7,9}
 #os dias eu fim de semana
uniao = conjunto1 | conjunto2
print(uniao) #imprime {5 ,10 ,3 ,7, 9}
intersecao = conjunto1 & conjunto2
print(intersecao) # imprime 5

diferenca = conjunto1 - conjunto2
print(diferenca) #IMPRIME {10,9}
diferenca_simetrica = conjunto1 ^ conjunto2
print(diferenca_simetrica) #imprime {5 ,10 ,3,7,9}
# dias desses tres janeiro , março, maio
# entao nesses dias que ficou dispnivel foram os dias 3 ,5,7,9,10 | 10,3,5| 3,5,7,9,10|
#entao agora ira selecionar nesse resultado final o dia e o mes da festa
# agora no resultado final a escolhar do mes e do dia da festa
mesdoano = {5,10,7,3,9}
mesdoano.add("dias")
print(mesdoano) #imprime {janeiro , março , maio}
# ele adicionou nessa varavel mes do ano os dias possiveis
mesdoano.remove("maio")
print(mesdoano) #imprime {"janeiro" , "março" , "maio"}
# o mes que foi tirado foi maio
mesdoano.remove("março")
print(mesdoano) # imprime {"janeiro"}
#  o mes que foi tirado foi o março
# agora resultado final o dia possivel para essa festa em janeiro
print(dias) #imprime {"10"}
# dia 10 o escolhido para festa
mesdoano.clear()
print(dias) #imprime set(5, 10, 7, 3, 9)
# ele imprime os dias da possivel escolhar da festa em janeiro que e o dia 10
# DIAS DA SEMANA
# janeiro dia 10