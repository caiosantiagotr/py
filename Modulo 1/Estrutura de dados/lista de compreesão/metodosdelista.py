#roupas = ["camisa" , "tenis" , "meia"]
#roupas = ["blusa" , "tenis da nike" , "presente"]
#roupas.append("celular")
#print(roupas) #imprime ["camisa" , "tenis" , "meia" , "celular"]
# importante ele adicionar o elemento "celular"
#importante append ele e (elemento que eu quero adicionar na variavel roupas)

#roupas.insert(3, "blusa" ,"tenis da nike" ,"presente")
#print(roupas) #imprime ["camisa" , "tenis" , "meia" "celular"]
#idicar o elemento na posiçao especifica


#roupas.remove("blusa" , "tenis da nike" , "presente")
#print(roupas)#imprime ["camisa" , "tenis" , "meia" , "celular"]


#roupas_removida = roupas.pop(2)
#print(roupas) #imprime ["blusa" , "tenis da nike" , "presente"]
#print(roupas_removida) #imprime "blusa"
# LISTA DE COMPREENSÃO
#nova_lista_de_roupas = [expressão for elemento in sequencia if condição]
#exemplo:
#numeros_de_lojas = [25, 1 , 8 , 0 ,6] # impares menos o numero 25
#quadrados_das_lojas = [x ** 2 for x in numeros_de_lojas if x % 2 == 0]
#print(quadrados_das_lojas) #imprime [6 , 2] 
# ele imprime os outros numeros de outras lojas nesse bairro que são numeros de 64, 0, 36 sao numeros pares
# numeros das lojas mas distante das outras lojas perto desse bairro
# que sao os numeros 25 , 1, 8, 0 ,6
# ele fitra os numeros pares [64 , 0 , 36]