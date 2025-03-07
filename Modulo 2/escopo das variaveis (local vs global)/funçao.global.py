varivel_global = 90
def funcao2():
    print(varivel_global) # acessivel de qualquer lugar
    funcao2() # imprime 10
    funcao2() # imprime 50
    print(varivel_global) # imprime 30
    print(varivel_global) # gerar um erro a varivel nao esta definida neste escopo
    # A funçao global sua varivel ela e definida fora da funçao e pode ser acessada em qualquer lugar