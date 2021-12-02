f=open('out','wb')
g=open('input.txt','rb')

def encrypt(bytearrayCuBytesLenKeyPls, keyPls):
    # print(bytearrayCuBytesLenKeyPls)
    for i in [(a ^ ord(b)) for a, b in zip(bytearrayCuBytesLenKeyPls , keyPls)]:
        f.write(i.to_bytes(1, 'big'))
        #Fișierul input.txt este mereu unul text. Fișierul output este unul binar, nu text (conține același număr de caractere ca și input.txt).
        #nu e binar in sensu ala


while 1:
    b=bytearray(g.read(10))
    if b != b'':
        encrypt(b, 'key???')
            
    else:
        break
