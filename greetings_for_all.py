#!/usr/bin/env python3

### chmod +x 'arquivo.py' (chmod é um comando para alterar a permissão de arquivos)

"""
    Classe C que fornece um metodo.

    A classe C é um exemplo simples que possui um metodo 
    chamado greetings, que caso não receba nenhum argumento retorne noble stranger, caso recebe algo que não seja uma str retorne Error! It was not a name
    e caso receber uma string retornar Hello {argumento}
    """

class C:
    def greetings(self, name="noble stranger"):

        """Método que exibe uma saudação com base no argumento fornecido.

        Args:
            name (str): O nome da pessoa a ser saudada. O padrão é "noble stranger".
        """
        
        if not isinstance(name, str):
            print("Error! It was not a name.") # Verifica se o argumento fornecido nao e uma string
        else:
            print(f"Hello, {name}") # Mostra Hello, com o argumento tipo string fornecido

c = C() # Criacao da instancia da classe C
c.greetings('Alexandra') #Chamando o metodo greetings com argumento em string
c.greetings('Wil') #Chamando o metodo greetings com argumento em string
c.greetings() #Chamando o metodo greetings sem argumentos
c.greetings(42) #Chamando o metodo greetings com argumento em inteiro


