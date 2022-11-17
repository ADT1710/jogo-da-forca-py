import random
from palavras import palavras
import string

def pega_palavra_valida(palavras):
    palavra = random.choice(palavras)
    while '-' in palavra or '' in palavra:
        word = random.choice(palavras)

    return palavra

def jogo_da_forca():
    palavra = pega_palavra_valida(palavras)
    letras_palavra = set(palavra)  # Letras na palavra
    alfabeto = set(string.ascii_uppercase)
    letras_utilizadas = set()  # Letras que o usuário advinhou

    # Pegando a entrada do usuário
    letra_do_usuario = input("Chute uma letra: ").upper()
    if letra_do_usuario in alfabeto - letras_utilizadas:
        letras_utilizadas.add(letra_do_usuario)
        if letra_do_usuario in letras_palavra:
            letras_palavra.remove(letra_do_usuario)

    elif letra_do_usuario in letras_utilizadas:
        print("Você já utilizou essa letra. Tente uma nova.")

    else:
        print('Caractere inválido. Tente novamente!')