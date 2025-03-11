from string import ascii_letters, punctuation, digits
import random

def passwd_generated(en_symbol=True, punc_symbol=True, digit=True, other_symbol=False, count=20):
    symbol = []

    if en_symbol:
        symbol += ascii_letters
    if punc_symbol:
        symbol += punctuation[0:9]
    if other_symbol:
        symbol += punctuation[9:]
    if digit:
        symbol += digits


    res_passwd = ''

    for _ in range(count):
        res_passwd += random.choice(symbol)

    return res_passwd

def id_passwd_generated(count=20):
    symbol = list(ascii_letters)
    res = ''

    for _ in range(count):
        res += random.choice(symbol)

    return res
