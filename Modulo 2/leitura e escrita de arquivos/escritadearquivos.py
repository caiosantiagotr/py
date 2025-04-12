# Neste exemplo, o arquivo "dados.txt" é aberto em modo de escrita utilizando open(). Depois, a string "Olá, mundo!" é escrita no arquivo utilizando o método write(). Finalmente, o arquivo é fechado utilizando o método close().
# Você também pode utilizar a declaração with para manejar a abertura e fechamento de arquivos de maneira automática.
#  Neste caso, o arquivo é aberto utilizando a declaração with e é fechado automaticamente uma vez que se sai do bloco with, mesmo se ocorrer uma exceção.
# A entrada e saída de dados em Python nos oferece uma grande flexibilidade para interagir com o usuário e manipular arquivos externos. Podemos solicitar informações ao usuário, mostrar resultados na tela e ler ou escrever dados em arquivos de texto. Lembre-se sempre de manejar adequadamente a abertura e fechamento de arquivos, e considerar as possíveis exceções que podem ocorrer durante as operações de entrada/saída.
# Para escrever dados em um arquivo, abrimos em modo de escrita ("w") utilizando a função open(). Se o arquivo não existir, será criado automaticamente. Se o arquivo já existir, seu conteúdo será sobrescrito.
#arquivo = open("dados.txt", "w")
#arquivo.write("Ola, caio!")
#arquivo.close()
with open("dados.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
# arquivo que ele fez abertura e o fechamento foi ola caio