#!/usr/bin/env python3

"""
Classe C que fornece método para adicionar 1 a uma variavel não mutavel.

Métodos:
adiciona 1 ao parametro passado

Importante notar que como a variavel number ela é imutavel, na resposta onde o valor atualizado deveria mostrar 2, mostra 1 e dentro do metodo se printar mostra 2,
isso se dá pela variavel number ser imutavel.
"""

import sys

number = 1 # considerado um parametro

class C:
    def add_one(self, one): # Adiciona 1 ao parametro passado.
        one += 1  
        print(one)

print("Initial value of number:", number) # Mostra a variavel
c = C()
c.add_one(number) # Chama o metodo add_one para adicionar 1
print("Updated value of number:", number) # Mostra a variavel atualizada depois de "adicionar" 1
