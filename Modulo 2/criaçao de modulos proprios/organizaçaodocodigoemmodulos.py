# operacoes.py
def somar(a,b):
   return a + b
def subtrair(a,b):
    return a - b
# utilidades.py
def imprimir_mensagem(mesagem):
    print(mesagem)

    def obter_nome_usuario():
       return input("digite seu nome:")
    import operacoes # type: ignore
    import utilidades # type: ignore
    resultado = operacoes.somar(5,3)
    utilidades.imprimir_mesagem(f"o resultado da soma e:{resultado}")
    nome = utilidades.obter_nome_usuario()
    utilidades.imprimir_mesagem(f"ola,{nome}!")