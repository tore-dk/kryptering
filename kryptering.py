import sys
import time

alphabet = "qwertyuiopåaäëüösdfghjklæø'<zxcvbnm,.-½1234567890+ QWERTYUIOPÅASDFGHJKLÆØZXCVBNM!#¤%&/()=?´`|>/*_;:"
key = 420420


def slow(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)


def encoder(cleartext, key):
    global alphabet
    final_list = []
    key = str(key)

    for letter in range(len(cleartext)):
        place = alphabet.find(cleartext[letter])
        step = int(key[letter % len(key)])
        final_list.append(alphabet[(place + step) % len(alphabet)])


def decoder(encrypted_text, key):
    global alphabet
    final_list = []
    for i in range(len(encrypted_text)):
        place = alphabet.find(encrypted_text[i])
#        displacement = den i'ende ciffer i key gange det i-1'ne ciffer i key
        final_list.append(alphabet[place - int(str(key)[i % len(str(key))])])
    return "".join(final_list)


while True:
    slow("vil du kryptere? [skriv 1], eller vil du DEkryptere? [skriv 2]")
    what_option = input()
    if what_option == "1":
        slow("hvilken besked vil du kryptere?")
        bravo_six_going_dark = input()
        slow(encoder(bravo_six_going_dark, key))
        print()
    elif what_option == "2":
        slow("hvad vil du dekryptere?")
        it_was_me_all_along = input()
        slow(decoder(it_was_me_all_along, key))
        print()


