# ele contem o codigo para gerar uma exceção ser ocorrer essa exceção ele e transferido para o bloco except
try: # codigo que pode gerar uma exceção ele gerar o ("divisao por zero")
    resultado = 10/ 0 # divisao pór zero
    print(resultado)
# ele e traferido para o except
except ZeroDivisionError:
    print("error: divisao por zero")
    # a variavel e o divisao por zero esse e o que ele vai imprimir