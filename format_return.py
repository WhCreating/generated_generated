import generated


def list_gener(en_symbol=True, punc_symbol=True, digit=True, other_symbol=False, count_pass=20, count=20):
    res = []

    for _ in range(count):
        a = generated.passwd_generated(en_symbol, punc_symbol, digit, other_symbol, count_pass)
        res.append(a)

    return res

def dict_gener(count_name = 20, en_symbol=True, punc_symbol=True, digit=True, other_symbol=False, count_pass=20, count=20):
    res = {}

    for _ in range(count):
        a = generated.id_passwd_generated(count_name)
        b = generated.passwd_generated(en_symbol, punc_symbol, digit, other_symbol, count_pass)
        res[a] = b

    return res

