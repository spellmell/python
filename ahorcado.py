# el ahorcado - v1 - WIP
# descarga del diccionario: https://bit.ly/3FFCIbP
# https://pastebin.com/ia8aDac9

import pandas as pd
import random as rnd
# colors
from sty import fg
from sty import Style, RgbFg

# cargar diccionario
cvsfile = "../../recursos/palabras.csv"
df = pd.read_csv(cvsfile, header=None, usecols=(["palabra"]),
                 names=["palabra"])

# colors
fg.green = Style(RgbFg(64, 255, 64))
fg.yellow = Style(RgbFg(255, 255, 64))
fg.red = Style(RgbFg(255, 64, 64))

valid_vocals = ["a", "á", "e", "é", "i", "í", "o", "ó", "u", "ú", "ü"]
valid_consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n",
                    "ñ", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]


def rng(lenq): return rnd.randint(0, lenq)


def get_palabra():
    palabra = (df["palabra"][rng(len(df["palabra"]))])
    return palabra.lower()


def ahorcado():
    palabra = get_palabra()
    palabra_temp = []
    intentos = 5
    print(f"\nAdivina la palabra!\nTienes {intentos} intentos...")

    lenp = len(palabra)
    for i in range(lenp):
        palabra_temp += "*"

    print(f"\n{fg.yellow}{lenp} letras: {''.join(palabra_temp)}{fg.rs}\n")

    j = 0
    letras_usadas = []
    while j < intentos:
        # input
        if len(letras_usadas) == 0:
            letra = str(input("Ingresa una letra: ")).lower()
        else:
            letra = str(input(
                f"Letras utilizadas: {'.'.join(letras_usadas).upper()}\n\n\
Ingresa una letra: ")).lower()
        # check
        if len(letra) > 1:
            intentos += -len(letra)
            print(f"\nDebes ingresar una única letra!\n\
Se te ha penalizado con -{len(letra)} intentos.\n")

        if letra not in letras_usadas and len(letra) == 1:
            letras_usadas.append(letra)
            if letra in valid_vocals or letra in valid_consonants:
                if letra in palabra:
                    pos = []
                    for k in range(lenp):
                        if palabra[k] == letra:
                            pos.append(k)
                            palabra_temp.pop(pos[-1])
                            palabra_temp.insert(pos[-1], letra)
                    # print(f"\nPosición de la {letra.upper()} {pos}")

                    print(
                        f"\n{fg.yellow}{lenp} letras: \
{''.join(palabra_temp).capitalize()}{fg.rs}\n\n\
Hay {palabra.count(letra)} {letra.upper()} en la palabra.\n")

                    if ''.join(palabra_temp).capitalize() \
                            == palabra.capitalize():
                        print(f"{fg.green}Enhorabuena, has ganado!{fg.rs}")
                        break
                else:
                    intentos += -1
                    print(
                        f"\nLa letra {letra.upper()} no está en la palabra.\n\
{fg.red}Intentos restantes: {intentos}{fg.rs}\n")
                    if intentos == 0:
                        print(
                            f"{fg.red}No lo has logrado!{fg.rs} \
La palabra era: {fg.green}{palabra.capitalize()}{fg.rs}\n\n\
>>>>>>>>>>>>>>>>>>>> GAME OVER <<<<<<<<<<<<<<<<<<<<")
                        break
            else:
                intentos += -1
                print(f"\n{letra} Nó es un caracter válido en una palabra.\n")
                print(f"{fg.red}Intentos restantes: {intentos}{fg.rs}\n")

    try:
        ahorcado()
    except KeyboardInterrupt:
        print("\nTerminado.")


try:
    ahorcado()
except KeyboardInterrupt:
    print("\nTerminado.")
