from textwrap import wrap


def decrypt(bytesOfLenKey, key):
    decrypted_text = ""
    for x, y in zip(wrap(bytesOfLenKey, 8), wrap(key, 8)):
        decrypted_text += chr((int(x, base=2) ^ int(y, base=2)))
    return decrypted_text


'''def encrypt(bytesOfLenKeyPls, keyPls):
    encrypted_text = ""
    if len(bytesOfLenKeyPls) < len(keyPls):
        bytesOfLenKeyPls = '\0' * (len(keyPls) - len(bytesOfLenKeyPls)) + bytesOfLenKeyPls

    for i in ['0' * (10 - len(bin(ord(a) ^ ord(b)))) + bin(ord(a) ^ ord(b))[2:] for a, b in
              zip(bytesOfLenKeyPls, keyPls)]:
        encrypted_text += i # aici e o mica modificare
    return encrypted_text''' # si aici
# am modificat putin si encryptul tau, pentru ca aveam nevoie
# de split() la decriptare
