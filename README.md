# Proiectu-ASC-cu-xor
Echipa adversa: power rangers

Noi: c0d3 8234k325

Cheia adversarilor : RMF14e2o2i5Mk

# Prima parte

```py
f=open('output','rb')
g=open('input.txt','rb')
k=open('cheie.txt','wb')

def encrypt(bytearrayCuBytesLenKeyPls, keyPls):
    for i in [(a ^ b) for a, b in zip(bytearrayCuBytesLenKeyPls , keyPls)]:
        k.write(i.to_bytes(1, 'big'))

b=bytearray(g.read(30))
ff=bytearray(f.read(30))
encrypt(b,ff)
```
**Doar deschidem ambele fisierele si facem xor unu la unu cu fiecare byte pentru a afisa cheia in fisierul 'cheie.txt'**

*Deoarece nu ii stim lungimea, o sa trebuiasca sa citim 30 de catactere, sa ne uitam noi la cele care se repeta si sa le taiem.* 
