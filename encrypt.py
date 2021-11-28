def encrypt(bytesOfLenKeyPls, keyPls):
    encrypted_text = ""
    if len(bytesOfLenKeyPls) < len(keyPls):
        bytesOfLenKeyPls = '\0' * (len(keyPls)-len(bytesOfLenKeyPls))+bytesOfLenKeyPls

    for i in [(ord(a) ^ ord(b)) for a, b in zip(bytesOfLenKeyPls, keyPls)]:
        print(i.to_bytes(1,'big'))
        #Fișierul input.txt este mereu unul text. Fișierul output este unul binar, nu text (conține același număr de caractere ca și input.txt).
        #nu e binar in sensu ala


        


