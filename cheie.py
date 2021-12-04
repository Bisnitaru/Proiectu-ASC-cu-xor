g=open('input.txt','rb')
k=open('cheie.txt','wb')

def encrypt(bytearrayCuBytesLenKeyPls, keyPls):
    for i in [(a ^ b) for a, b in zip(bytearrayCuBytesLenKeyPls , keyPls)]:
        k.write(i.to_bytes(1, 'big'))

b=bytearray(g.read(30))
ff=bytearray(f.read(30))
encrypt(b,ff)