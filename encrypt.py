def enc(bytesOfLenKeyPls, keyPls):

    #pad cu 0
    if len(bytesOfLenKeyPls) < len(keyPls):
        bytesOfLenKeyPls = '\0' * (len(keyPls)-len(bytesOfLenKeyPls))+bytesOfLenKeyPls
            
    for i in ['0'*(10-len(bin(ord(a) ^ ord(b))))+bin(ord(a) ^ ord(b))[2:] for a, b in zip(bytesOfLenKeyPls, keyPls)]:
        print(i)
        



