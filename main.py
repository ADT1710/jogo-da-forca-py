import random
from palavras import palavras
import string

def pega_palavra_valida(palavras):
    palavra = random.choice(palavras)
    while '-' in palavra or ' ' in palavra:
        palavra = random.choice(palavras)


    return palavra

def jogo_da_forca():
    palavra = pega_palavra_valida(palavras).upper()
    print(palavra)
    letras_palavra = set(palavra.upper())  # Letras na palavra
    print(letras_palavra)
    alfabeto = set(string.ascii_uppercase)
    letras_utilizadas = set()  # Letras que o usuário advinhou
    lista_de_letras = []
    for letra in palavra:
        lista_de_letras.append("-")

    vidas = 6

    # Pegando a entrada do usuário
    while len(letras_palavra) > 0 and vidas > 0:
        # Letras utilizadas
        print(f'Vidas atuais {vidas}. Você já utilizou essas letras: ', ' '.join(letras_utilizadas))


        letra_do_usuario = input("Palpite a letra desejada: ").upper()
        if letra_do_usuario in alfabeto - letras_utilizadas:
            letras_utilizadas.add(letra_do_usuario)
            if letra_do_usuario in letras_palavra:
                letras_palavra.remove(letra_do_usuario)

                # Estado atual da palavra adivinhada
                for index,letra in enumerate(palavra):
                    if palavra[index] == letra_do_usuario:
                        lista_de_letras[index] = letra_do_usuario
                print(lista_de_letras)

            else:
                vidas = vidas - 1
                print('Essa letra não está na palavra!')

        elif letra_do_usuario in letras_utilizadas:
            print("Você já utilizou essa letra. Tente uma nova.")

        else:
            print('Caractere inválido. Tente novamente!')

    if vidas == 0:
        print(f'Você perdeu, tente novamente! A palavra era {palavra}')
    else:
        print(f'Você adivinhou a palavra, que era: {palavra}!')

jogo_da_forca()