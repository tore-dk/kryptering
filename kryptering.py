import random
import string

alphabet = "qwertyuiopåaäëüösdfghjklæø'<zxcvbnm,.-½1234567890+ QWERTYUIOPÅASDFGHJKLÆØZXCVBNM!#¤%&/()=?´`|>/*_;:"
key = 420420


def encoder(cleartext, key):  # alt skal være i lowercase indtil videre # OG UDEN ÆØÅ ### DET VIRKER NÆSTEN ###
    global alphabet
    final_list = []  # husk at joine string til sidst
    key = str(key)

    for letter in range(len(cleartext)):
        cont = True
        for j in range(len(alphabet)):
            if cleartext[letter] == alphabet[j] and cont:
                step = int(key[letter % len(key)])
                final_list.append(alphabet[(j + step) % len(alphabet)])
                cont = False
        if cont:
            final_list.append(cleartext[letter])
    return "".join(final_list)


def decoder(encrypted_text, key):
    global alphabet
    final_list = []
    for i in range(len(encrypted_text)):
        place = alphabet.find(encrypted_text[i])
#        displacement = den i'ende ciffer i key gange det i-1'ne ciffer i key
        final_list.append(alphabet[place - int(str(key)[i % len(str(key))])])
    return "".join(final_list)


while True:
    what_option = input("vil du kyptere? [skriv 1], eller vil du DEkryptere? [skriv 2]")
    if what_option == "1":
        bravo_six_going_dark = input("hvilken besked vil du kyptere?")
        print(encoder(bravo_six_going_dark, key))
    elif what_option == "2":
        it_was_me_all_along = input("hvad vil du dekryptere?")
        print(decoder(it_was_me_all_along, key))


