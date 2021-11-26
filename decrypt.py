from textwrap import wrap


def decrypt(bytesOfLenKey, key):
    decrypted_text = ""
    for x, y in zip(wrap(bytesOfLenKey, 8), wrap(key, 8)):
        decrypted_text += chr((int(x, base=2) ^ int(y, base=2)))
    return decrypted_text
