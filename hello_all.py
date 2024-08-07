#!/usr/bin/env python3

### chmod +x 'arquivo.py' (chmod é um comando para alterar a permissão de arquivos)

"""
    Classe C que fornece um metodo.

    A classe C é um exemplo simples que possui um metodo 
    chamado hello, que imprime algo na tela.
    """

str_hello = "Hello,everyone!" # Cria uma variavel Hello

class C:
    def hello(self):
        print(f"{str_hello}") # Esse metodo exibe a mensagem

c = C() # Criacao da instancia da classe C
c.hello() #Chamando o metodo hello
