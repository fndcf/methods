#!/usr/bin/env python3

### chmod +x 'arquivo.py' (chmod é um comando para alterar a permissão de arquivos)

"""
    Classe C que fornece um metodo.

    A classe C é um exemplo simples que possui um metodo 
    chamado upcase_it, que imprime na tela a variavel que foi passada em letra maiuscula.
    """

str_hello = "hello" # Cria uma variavel hello

class C:
    def upcase_it(self):
        print(f"{str_hello.upper()}") # Esse metodo Imprime a string com letra maiscula

c = C() # Criacao da instancia da classe C
c.upcase_it() #Chamando o metodo upcase