# Em Python, a entrada e saída de dados nos permite interagir com o usuário e manipular arquivos. 
nome = input("insire seu nome:")
idade = input("insira sua idade:")
print("ola," +nome+ "!")
print("voce tem"+idade+"anos.")
# para obter a informação do usuario temos que utilizar o input
# a informação do usuario sao os input()
# os valores inseridos sao armazenados nas variveis idade e nome
idade = int(input("insira sua idade:"))

if idade <=18:
   print("voce e menor de idade")
else:
    print("voce e maior de idade")