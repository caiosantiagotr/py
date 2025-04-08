# dicionario numero 1 que foi criando no inicio
pessoa_da_loja = {"nome": "maria" , "idade": 18, "cidade": "sao paulo"}
print(pessoa_da_loja.keys()) #imprime dict_keys(["nome," "idade 18" , "cidade"])
# keys el retornar na visualizaçao de todas as chaves
# as chaves sao os valores maria , idade , cidade
# ele excluir  maria , 18 e sao paulo e focou que sao as chaves nome , idade , cidade
# o keys ele nao pegar a informaçao toda
print(pessoa_da_loja.values()) #imprime dict_values(["maria" , 18, "sao paulo"])
# ele retornar os valores da variavel pessoa_da_loja
# ele imprime tudo junto
print(pessoa_da_loja.items()) #imprime dict_items([("nome" , maria)]), ("idade , 18") , ("cidade, " "sao paulo")])
# ele imprime os valores da variavel de cada chve separando uma por uma
# e esse dicionario atualizado o dicionario numero 1
#pessoa_da_loja.update({"profissao": "medica"})
print(pessoa_da_loja) #imprime {"nome": "maria", "idade": 18 , "cidade": "sao paulo", "profissao": "medica"}
# ele criar outro dicionario com outra informaçao que nao tinha antes e atualizar o dicionario  que existe
# ser antes eu tinha o nome , idade , cidade agora eu tenho profissao: medica em um so dicionario
# outro dicionario e adiciono no diconario da variavel pessoa_da_loja
# profissao : medica e o elemento que eu quero adicionar na variavel pessoa _da_loja