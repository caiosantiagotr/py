def funcao():
    # codigo que pode gerar uma exceçao personalizada
    if funcao:
        raise Exception("descriçao do meu celular")
    try: 
        funcao()
    except Exception as e:
        print(f"Erro: {str(e)}")

        # IMPORTANTE?
        # Considere os possíveis erros que podem ocorrer no seu código e utilize o tratamento de exceções adequado para lidar com eles de maneira apropriada. Isso tornará seus programas mais robustos e confiáveis.