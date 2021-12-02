f=open('output.txt','wb')
g=open('input.txt','rb')

def encrypt(bytearrayCuBytesLenKeyPls, keyPls):
    for i in [(a ^ ord(b)) for a, b in zip(bytearrayCuBytesLenKeyPls , keyPls)]:
        f.write(i.to_bytes(1, 'big'))


while 1:
    b=bytearray(g.read(10))
    if b != b'':
        encrypt(b, 'key???')      
    else:
        break
