def encrypt(bytesOfLenKeyPls, keyPls):
    encrypted_text = ""
    if len(bytesOfLenKeyPls) < len(keyPls):
        bytesOfLenKeyPls = '\0' * (len(keyPls) - len(bytesOfLenKeyPls)) + bytesOfLenKeyPls
        
    for i in ['0' * (10 - len(bin(ord(a) ^ ord(b)))) + bin(ord(a) ^ ord(b))[2:] for a, b in zip(bytesOfLenKeyPls, keyPls)] 
        encrypted_text += i
        
    return encrypted_text
        



