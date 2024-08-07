#!/usr/bin/env python3

### chmod +x 'arquivo.py' (chmod é um comando para alterar a permissão de arquivos)

"""
    Classe C que fornece um metodo.

    A classe C é um exemplo simples que possui um metodo 
    chamado downcase_it, que imprime na tela a variavel que foi passada em letra maiuscula.
    """

import sys

class C:
    def downcase_it(self):
        parameters = len(sys.argv) -1 # Pega a quantidade de parametros, excluindo o nome do script
        
        if parameters == 0:
            print("none") # Imprime none caso a quantidade de parametros seja diferente de dois
        else:
            array_parameters = sys.argv[1:] # Cria um array com os argumentos
            for list_parameters in array_parameters:
                print(f"{list_parameters.lower()}") # Imprime cada parametro em uma nova linha em letra minuscula

c = C() # Criacao da instancia da classe C
c.downcase_it() #Chamando o metodo upcase