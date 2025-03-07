# ele permite um numero variavel de argumentos utilizado o operador antes do parametro.
def soma_variavel(*numeros):
    total = 0
    for numero in numeros:
        total += numero
        return total
    print(soma_variavel)(4,7,9) # imprime 1
    print(soma_variavel)(2,6,5) # imprime 33
    # as funçoes sao uma ferramenta da progrmaçao e definir as funçoes
    # funçoes que o python fornece sao print(), len() , range()
    # a funçao mas que utilizamos ate aqui no inicio e fim do modulo 1 e nesse inicio de modulo 2 
    # e a funçao print()
    # ele retona na varivel soma dos numeros
    # no seu total
    # depois ele somar os numeros
    # pra fazer o resultado final
    # ele volta ao total da soma da variavel que e os numeros
    # e imprime o resultado da variavel soma