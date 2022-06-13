# Random names generator # v3 syllables : WIP
# https://pastebin.com/D5aDNXNd

import random as rnd
import sys

savefile = (f"{sys.argv[0].split('.')[0]}.txt")
savename = True
printsavednames = True

# No más de 2 consonantes juntas.
# Vocales no van juntas.
# Nombres y apellidos con no más de 8 caracteres.
# Primera letra de nombre y apellido capitalizada.


def r_names_g():
    name = []
    surname = []
    minlen_characters = 4
    maxlen_characters = 8
    def rng(): return rnd.randint(minlen_characters, maxlen_characters)
    vocals = ("a", "e", "i", "o", "u")
    # vocals = ("a", "á", "e", "é", "i", "í", "o", "ó", "u", "ú", "ü")
    consonants = ("b", "c", "d", "f", "g", "h", "j", "k", "l", "m",
                  "n", "ñ", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z")

    def letter_v(): return vocals[rnd.randint(0, len(vocals)-1)]
    def letter_c(): return consonants[rnd.randint(0, len(consonants)-1)]
    syll2 = []
    syll3 = []
    # 9, 36, 54, 63, 153, 351. 64, 128, 256, 512, 1024, 2048, 3072, 4096.
    syll_loops = 4096
    def syll(): return ''.join([syll2[rng()], syll3[rng()]])

    s1 = 0
    while s1 <= syll_loops:
        if rng() % 2 == 0:
            syll2.append(''.join([letter_c(), letter_v()]))
        else:
            syll2.append(''.join([letter_v(), letter_c()]))
        s1 = s1+1

    s2 = 0
    while s2 <= syll_loops:
        if rng() % 2 == 0:
            syll3.append(''.join([letter_c(), letter_v(), letter_c()]))
        else:
            syll3.append(''.join([letter_v(), letter_c(), letter_v()]))
        s2 = s2+1

    i = 0
    while i <= syll_loops:
        name.append(syll())
        surname.append(syll())
        i = i+1

    name = (''.join(name))
    name = name[:rng()].capitalize()
    surname = (''.join(surname))
    surname = surname[:rng()].capitalize()

    if savename:
        savenames(savename, printsavednames, savefile, name, surname)

    return str(f"{name} {surname}")


def generar_nombres(cuantos):
    list_names = []
    def new_name(): return r_names_g()
    for x in range(cuantos):
        nn = new_name()
        list_names.append(nn)
    return list_names


def savenames(state, printsavednames, rute, name, surname):
    if state and rute:
        saved_names_file = open(rute, "a", encoding='utf-8')
        saved_names_file.write(f"{name} {surname}\n")
        saved_names_file.close()
    if printsavednames:
        saved_names_file = open(rute, "r", encoding='utf-8')
        all_saved_names = saved_names_file.readlines()
        all_saved_names = [x[:-1] for x in all_saved_names]
        print(
            f"\n{all_saved_names}\nHay {len(all_saved_names)} \
nombres guardados.")


# generar uno
# print(f"\n{r_names_g()}\n")

# generar multiples
print(generar_nombres(int(input("Ingresa el número de nombres que quieres generar: "))))
