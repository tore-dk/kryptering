#!/usr/bin python3
import sys
import time

alphabet = "qwertyuiopåaäëüösdfghjklæø'<zxcvbnm,.-½1234567890+ QWERTYUIOPÅASDFGHJKLÆØZXCVBNM!#¤%&/()=?´`|>/*_;:"
myKey = "TOREOGTOKE" # Det er i base 36. Det bliver konverteret senere :). Desuden er det en string husk lige det
base = 36


def slow(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)


def encoder(cleartext, key): # key gives som et hexadecimal-tal
    global alphabet
    final_list = []
    key = str(key)
    keysum = 0
    for i in key:
        keysum += int(i, base)

    for letter in range(len(cleartext)):
        place = alphabet.find(cleartext[letter])
        step = int(key[letter % len(key)], base) + keysum + len(cleartext)
        final_list.append(alphabet[(place + step) % len(alphabet)])
    return "".join(final_list)


def decoder(encrypted_text, key): # key gives (igen) som et hexadecimal-tal
    global alphabet
    final_list = []
    keysum = 0
    for i in key:
        keysum += int(i, base)

    for i in range(len(encrypted_text)):
        place = alphabet.find(encrypted_text[i])
        displacement = int(str(key)[i % len(str(key))], base) + keysum + len(encrypted_text)
        final_list.append(alphabet[(place - displacement) % len(alphabet)])
    return "".join(final_list)


while True:
    slow("vil du kryptere? [skriv 1], eller vil du DEkryptere? [skriv 2]")
    what_option = input()
    if what_option == "1":
        slow("hvilken besked vil du kryptere?")
        bravo_six_going_dark = input()
        slow(encoder(bravo_six_going_dark, myKey))
        print()
    elif what_option == "2":
        slow("hvad vil du dekryptere?")
        it_was_me_all_along = input()
        slow(decoder(it_was_me_all_along, myKey))
        print()


