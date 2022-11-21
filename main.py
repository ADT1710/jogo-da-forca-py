import random
from palavras import palavras
import string

def pega_palavra_valida(palavras):
    palavra = random.choice(palavras)
    while '-' in palavra or ' ' in palavra:
        palavra = random.choice(palavras)


    return palavra

def jogo_da_forca():
    palavra = pega_palavra_valida(palavras)
    print(palavra)
    letras_palavra = set(palavra.upper())  # Letras na palavra
    print(letras_palavra)
    alfabeto = set(string.ascii_uppercase)
    letras_utilizadas = set()  # Letras que o usuário advinhou

    # Pegando a entrada do usuário
    while len(letras_palavra) > 0:
        # Letras utilizadas
        print('Você já utilizou essas letras: ', ' '.join(letras_utilizadas))

        # Estado atual da palavra adivinhada
        lista_de_letras = [letra if letra in letras_utilizadas else '-' for letra in palavra]
        print(lista_de_letras)
        print('Estado atual da palavra: ', ' '.join(lista_de_letras))

        letra_do_usuario = input("Palpite a letra desejada: ").upper()
        if letra_do_usuario in alfabeto - letras_utilizadas:
            letras_utilizadas.add(letra_do_usuario)
            if letra_do_usuario in letras_palavra:
                letras_palavra.remove(letra_do_usuario)


        elif letra_do_usuario in letras_utilizadas:
            print("Você já utilizou essa letra. Tente uma nova.")

        else:
            print('Caractere inválido. Tente novamente!')

jogo_da_forca()