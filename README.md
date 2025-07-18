# Curso de Python - Material de Estudo

Este repositório contém material didático para aprendizado da linguagem Python, organizado em dois módulos principais que cobrem desde conceitos básicos até tópicos mais avançados.

## 📚 Estrutura do Curso

### Módulo 1 - Fundamentos

#### Conceitos Básicos
- **Introdução ao Python** (`introduçao.py`)
  - Estruturas condicionais básicas
  - Comentários (linha única e múltiplas linhas)
  - Sintaxe fundamental

- **Tipos de Dados**
  - `inteiros.py` - Números inteiros
  - `float.py` - Números decimais  
  - `texto.py` - Strings e texto
  - `booleanos.py` - Valores True/False

#### Operadores
- **Operadores Aritméticos** (`Operadores.py`)
  - Soma, subtração, multiplicação, divisão
  - Divisão inteira, módulo, exponenciação
  
- **Operadores de Comparação** (`comparação.py`)
  - Igualdade (==), diferença (!=)
  - Maior (>), menor (<), maior igual (>=), menor igual (<=)

- **Operadores Lógicos** (`Logicos.py`)
  - AND, OR, NOT
  - Combinação de condições

#### Estruturas de Controle
- **Condicionais** (`Controle.py`, `controle2.py`)
  - if, elif, else
  - Estruturas de decisão

- **Loops** 
  - `for.py` - Loops com sequências
  - `while.py` - Loops condicionais
  - `continue.py` - Controle de fluxo
  - `pass.py` - Placeholder

#### Estruturas de Dados

##### Listas
- `Lista.py`, `lista2.py` - Criação e acesso a elementos
- `metodosdelista.py` - Métodos append, insert, remove, pop
- `remove.py` - Remoção de elementos
- Lista de compreensão para criação eficiente

##### Tuplas
- `Tuplas.py` - Estruturas imutáveis
- `metodosdetuplas.py` - Métodos index, count, len

##### Conjuntos (Sets)
- `conjuntos.py` - Operações com conjuntos
- União, interseção, diferença, diferença simétrica
- Métodos add, remove, clear

##### Dicionários
- `dicionario.py` - Estrutura chave-valor
- `Metodosdedicionarios.py` - keys(), values(), items(), update()

### Módulo 2 - Conceitos Avançados

#### Entrada e Saída de Dados
- **Entrada de Dados** (`entradadedadosdousuario.py`)
  - Função input()
  - Conversão de tipos
  
- **Saída de Dados** (`saidadedados.py`)
  - Função print()
  - F-strings para formatação

#### Funções
- **Definição de Funções** (`funções.py`)
  - Definição com def
  - Parâmetros e argumentos
  - Valores de retorno

- **Funções Avançadas**
  - `funçoesanonimas.py` - Funções lambda
  - `variaveldeargumentos.py` - *args para argumentos variáveis
  - `docstrings.py` - Documentação de funções

#### Escopo de Variáveis
- `funçoeslocal.py` - Variáveis locais
- `funçao.global.py` - Variáveis globais
- Diferenças entre escopo local e global

#### Módulos e Pacotes
- **Importação** (`importaçao.py`)
  - import e from...import
  - Uso de módulos padrão

- **Módulos Padrão** (`funçaoeclassesdemodulospadrao.py`)
  - math - Funções matemáticas
  - random - Números aleatórios
  - datetime - Datas e horas

- **Módulos Personalizados** (`modulopersonalizado.py`)
  - Criação de módulos próprios
  - `organizaçaodocodigoemmodulos.py` - Organização de código

- **Pacotes** (`pacotes.py`)
  - Estrutura hierárquica de módulos
  - Organização em diretórios

#### Tratamento de Erros
- **Tipos de Erros** (`Tratamento.py`)
  - SyntaxError - Erros de sintaxe
  - NameError - Variáveis não definidas
  - TypeError - Incompatibilidade de tipos
  - IndexError - Índices fora do intervalo

- **Tratamento de Exceções**
  - `try.py` - Bloco try para código que pode gerar exceção
  - `Except.py` - Captura e tratamento de exceções
  - `Finally.py` - Código executado sempre
  - `exceçoes.py` - Exceções personalizadas

#### Manipulação de Arquivos
- **Leitura** (`leituradearquivos.py`)
  - Abertura em modo leitura ("r")
  - Métodos read() e readlines()

- **Escrita** (`escritadearquivos.py`)
  - Abertura em modo escrita ("w")
  - Método write()
  - Uso da declaração with

## 🚀 Como Usar Este Material

1. **Começe pelo Módulo 1**: Estude os conceitos básicos na ordem apresentada
2. **Pratique os Exemplos**: Execute cada arquivo .py para ver os conceitos em ação
3. **Avance para o Módulo 2**: Após dominar os fundamentos
4. **Experimente**: Modifique os códigos para entender melhor

## 📝 Observações Importantes

- Alguns arquivos contêm comentários em português explicando os conceitos
- Os exemplos são práticos e demonstram uso real dos conceitos
- Há alguns erros de sintaxe intencionais em arquivos de exemplo sobre tratamento de erros
- O material inclui tanto teoria quanto prática

## 🎯 Objetivos de Aprendizado

Ao completar este curso, você será capaz de:
- Compreender a sintaxe básica do Python
- Trabalhar com diferentes tipos de dados
- Implementar lógica de programação com estruturas de controle
- Manipular estruturas de dados complexas
- Criar e organizar código em funções e módulos
- Tratar erros de forma apropriada
- Realizar entrada/saída de dados e manipulação de arquivos

## 📁 Estrutura de Arquivos

```
Modulo 1/
├── Conceitos básicos (introdução, tipos de dados)
├── Operadores (aritméticos, comparação, lógicos)
├── Estruturas de controle (if/else, loops)
└── Estruturas de dados (listas, tuplas, conjuntos, dicionários)

Modulo 2/
├── Entrada e Saída de dados
├── Funções (definição, lambda, escopo)
├── Módulos e Pacotes
├── Tratamento de Exceções
└── Manipulação de Arquivos
```

## 🤝 Contribuições

Este é um material didático em constante evolução. Sugestões e melhorias são bem-vindas!

---

**Nota**: Este material foi desenvolvido para fins educacionais e contém exemplos práticos para facilitar o aprendizado da linguagem Python.
