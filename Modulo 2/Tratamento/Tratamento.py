# Error de Sintaxe (SyntaxError)
# nao segue as regras da sintaxe
# def uma declaração
 #def meu_funcao() 
 # falta os dois pontos

#print("nome")
# Error de nome (NameError)
#print(variavel_nao_definida)
# quando nao a difinição da varivel da funçao que nao foi encontrada
# e por isso da o error de nome
#Error de tipo (TypeError)
#resultado = 4 + "20"
# o error do resultado
# Traceback (most recent call last):
  #File "c:\Users\Windows\Downloads\py\Modulo 2\Tratamento.py", line 13, in <module>
   # resultado = 4 + "20"
    #            ~~^~~~~~
 #TypeError: unsupported operand type(s) for +: 'int' and 'str'
 # ocorrer o error quando os valores nao sao iguais.
# Error de indice (IndexError)
#listacarro = ["azul" , "amarelo" , "vermelho"]
#print(listacarro["vermelho"]) # o indice vermelho esta fora do intervalo
# o vermelho esta fora do indice da listacarro
#Estes são apenas alguns exemplos de erros comuns. Quando ocorre um erro, Python gera uma exceção e exibe uma mensagem de erro que inclui o tipo de exceção e uma descrição do problema.