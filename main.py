import random
from palavras import palavras

def pega_palavra_valida(palavras):
    palavra = random.choice(palavras)
    while '-' in palavra or '' in palavra:
        word = random.choice(palavras)

    return palavra