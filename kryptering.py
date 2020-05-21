#!/usr/bin python3
import sys
import time

alphabet = "qwertyuiopåaäëüösdfghjklæø'<zxcvbnm,.-½1234567890+ QWERTYUIOPÅASDFGHJKLÆØZXCVBNM!#¤%&/()=?´`|>/*_;:"
myKey = "6F5EE78" # husk at convert hex til deci senere


def slow(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)


def encoder(cleartext, key): # key gives som et hexadecimal-tal
    global alphabet
    final_list = []
    key = str(key)

    for letter in range(len(cleartext)):
        place = alphabet.find(cleartext[letter])
        step = int(key[letter % len(key)], 16)
        final_list.append(alphabet[(place + step) % len(alphabet)])
    return "".join(final_list)


def decoder(encrypted_text, key): # key gives (igen) som et hexadecimal-tal
    global alphabet
    final_list = []
    for i in range(len(encrypted_text)):
        place = alphabet.find(encrypted_text[i])
        displacement = int(str(key)[i % len(str(key))], 16)
        final_list.append(alphabet[place - displacement])
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


