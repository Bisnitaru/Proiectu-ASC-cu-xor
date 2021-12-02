f = open('input_recuperat.txt','wb')
g = open('output.txt','rb')


def decrypt(bytearrayCuBytesLenKeyPls, keyPls):
    for i in [(a ^ ord(b)) for a, b in zip(bytearrayCuBytesLenKeyPls, keyPls)]:
        f.write(i.to_bytes(1, 'big'))


while 1:
    b = bytearray(g.read(10))
    if b != b'':
        decrypt(b, 'ZUXUv6T6sb')
    else:
        break
