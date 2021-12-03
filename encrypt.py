import sys
f=open(sys.argv[3],'wb')
g=open(sys.argv[2],'rb')

def encrypt(bytearrayCuBytesLenKeyPls, keyPls):
    print(bytearrayCuBytesLenKeyPls)
    for i in [(a ^ ord(b)) for a, b in zip(bytearrayCuBytesLenKeyPls , keyPls)]:
        f.write(i.to_bytes(1, 'big'))


while 1:
    b=bytearray(g.read(len(sys.argv[1])))
    if b != b'':
        encrypt(b, sys.argv[1])
            
    else:
        break
