from textwrap import wrap

f = open('output.txt', 'wb')
g = open('input.txt', 'rb')


def decrypt(bytearrayCuBytesLenKeyPls, keyPls):
    for i in [(a ^ ord(b)) for a, b in zip(bytearrayCuBytesLenKeyPls, keyPls)]:
        m.write(i.to_bytes(1, 'big'))

def encrypt(bytearrayCuBytesLenKeyPls, keyPls):
    for i in [(a ^ ord(b)) for a, b in zip(bytearrayCuBytesLenKeyPls, keyPls)]:
        f.write(i.to_bytes(1, 'big'))

while 1:
    b = bytearray(g.read(10))
    if b != b'':
        encrypt(b, 'ZUXUv6T6sb')
    else:
        break

f.close()
g.close()

h = open("output.txt", 'rb')
m = open("input_recuperat.txt", 'wb')

while 1:
    a = bytearray(h.read(10))
    if a != b'':
        decrypt(a, 'ZUXUv6T6sb')
    else:
        break

h.close()
m.close()
