#!/usr/bin/env python3

"""
Classe C que fornece métodos para manipulação de strings.

Métodos:
- shrink: Exibe os primeiros 8 caracteres de uma string.
- enlarge: Completa uma string com 'Z' até completar 8 caracteres.
- process_strings: Processa uma lista de strings conforme as regras:
  - Se a string tiver menos de 8 caracteres, chama enlarge.
  - Se a string tiver mais de 8 caracteres, chama shrink.
  - Se a string tiver exatamente 8 caracteres, exibe a string.
  - Se a lista de strings estiver vazia, exibe "none".
"""

import sys

class C:
    def shrink(self, string): 
        x = slice(0, 8)
        print(string[x]) # Exibe os primeiros 8 caracteres da string.

    def enlarge(self, string):
        print(string + 'Z' * (8 - len(string))) # Completa uma string com 'Z' até completar 8 caracteres.

    def process_strings(self, parameters): # Processa uma lista de strings conforme as regras especificadas, caso não tenha nenhum parametro, mostra none e da um return para finalizar.        
        if len(parameters) < 1:
            print("none")
            return
        for string in parameters:
            if len(string) < 8:
                self.enlarge(string)  # Chama enlarge para strings com menos de 8 caracteres
            elif len(string) > 8:
                self.shrink(string)  # Chama shrink para strings com mais de 8 caracteres
            else:
                print(string)  # Exibe a string se tiver exatamente 8 caracteres

parameters = sys.argv[1:]  
c = C()
c.process_strings(parameters)
