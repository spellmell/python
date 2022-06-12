# Random text generator v3
# https://pastebin.com/JvYUdTcr

import re
import random as rnd

num_words = 4096

minlen_characters = 5
maxlen_characters = 8
comas = [",", ",", ",", ";", ";", "."]
vocals = ("a", "e", "i", "o", "u")
vocals_t = ("á", "é", "í", "ó", "ú", "ü")
consonants = ("b", "c", "d", "f", "g", "h", "j", "k", "l", "m",
              "n", "ñ", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z")


def rng(): return rnd.randint(minlen_characters, maxlen_characters)
def letter_v(): return vocals[rnd.randint(0, len(vocals)-1)]
def letter_vt(): return vocals_t[rnd.randint(0, len(vocals_t)-1)]
def letter_c(): return consonants[rnd.randint(0, len(consonants)-1)]


def spacesCleaner(stringText):
    stringText = list(stringText)
    text2Check = []
    subStringLen = 6
    maxSpacesAllowed = 1
    try:
        for i in stringText:
            text2Check.append(i)
            iIndex = stringText.index(i)
            if i == " " and text2Check.count(" ") > maxSpacesAllowed:
                # stringText.pop(stringText.index(i))
                stringText[iIndex-subStringLen:iIndex] = []
                stringText.insert(iIndex, letter_c()+letter_vt()
                                  + letter_c()+letter_vt()+letter_c())
            if len(text2Check) > subStringLen:
                text2Check.pop(0)
    except ValueError:
        pass

    return stringText


def pushComas(stringText):
    stringText = list(stringText)
    maxComas = 360
    def comaRand(): return comas[rnd.randint(0, len(comas))-1]
    c = 0
    while c <= maxComas:
        stringText.insert(rnd.randint(0, len(stringText)),
                          letter_c()+comaRand())
        c += 1
    return stringText


def r_text_g(num_words):
    text, syll2, syll3, syll4 = [], [], [], []

    syll_loops = 4096
    def syll(): return ''.join([syll2[rng()], syll3[rng()], syll4[rng()]])

    s1 = 0
    while s1 <= syll_loops:
        rand = rng()
        if rand % 2 == 0:
            syll2.append(''.join([letter_c(), letter_v()]))
        else:
            syll2.append(''.join([letter_v(), letter_c()]))
        s1 = s1+1
        # randchecknums_147 = [rng()]
        # if rand in randchecknums_147 and int(str(s1)[-1]) % 2 == 0:
        #     syll2.append('. ')

    s2 = 0
    while s2 <= syll_loops:
        rand = rng()
        if rand % 2 == 0:
            syll3.append(''.join([letter_c(), letter_v(), letter_c()]))
        else:
            syll3.append(''.join([letter_v(), letter_c(), letter_v()]))
        s2 = s2+1
        # randchecknums_258 = [rng()]
        # if rand in randchecknums_258 and int(str(s2)[-1]) % 2 == 0:
        #     syll3.append(', ')

    s3 = 0
    while s3 <= syll_loops:
        rand = rng()
        if rand % 2 == 0:
            syll4.append(
                ''.join([letter_c(), letter_v(), letter_c(), letter_v()]))
        else:
            syll4.append(
                ''.join([letter_v(), letter_c(), letter_v(), letter_c()]))
        s3 = s3+1
        # randchecknums_369 = [rng()]
        # if rand in randchecknums_369 and int(str(s3)[-1]) % 2 == 0:
        #     syll4.append('; ')

    i = 0
    while i <= num_words:
        text.append(syll())
        i += 1

    # add letters in randoms positions
    # alteración del largo de subcadenas para quebrar monotonia
    # en el largo de las palabras
    j = 0
    while j <= num_words:
        def rndIndex(): return rnd.randint(0, len(text)-1)
        rJupmp2Index = rndIndex()
        if rJupmp2Index <= len(text):
            joIn = (letter_vt()+letter_c()+letter_v()
                    + ''.join(text)[rJupmp2Index:rJupmp2Index+1])
        else:
            joIn = (letter_vt()+letter_c()+letter_v()
                    + ''.join(text)[rJupmp2Index:])
        text.pop(rJupmp2Index)
        text.insert(rJupmp2Index, joIn)
        j += 1

    # spaces cleaner
    text = spacesCleaner(text)

    # agregar comas
    text = pushComas(text)

    text = (' '.join(text))
    # text = re.sub(r"[" ","  ","   "]", ", ", text)
    text = re.sub(r"[^a-zA-Z0-9"+str(vocals_t)+str(comas)+"]+",
                  letter_v(), text)
    # elimina todos los caracteres no ascii de la cadena
    # text = re.sub(r"[^\x00-\x7f]", r"", text)
    # � = b'\xef\xbf\xbd'
    # text = re.sub("\xef\xbf\xbd", "", text)

    return str(f"{text.capitalize()}")


# generar texto de parrafo
print(f"{r_text_g(num_words)}")
