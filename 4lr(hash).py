import random as rd
def shift(tx, step):
    if step < 0:
        step = abs(step)
        for i in range(step):
            tx.append(tx.pop(0))
    else:
        for i in range(step):
            tx.insert(0,tx.pop())
    return tx

def hash(st):
    res,c,ls,buf="",0,[],0
    for i in st:
        c+=ord(i)
    k=int(c/len(st))
    for i in st:
        n=ord(i)
        b=0
        j = 1
        while n:
            n, enc=divmod(n,3)
            b+=enc*j
            j *= 10
        while b:
            s=b%10
            b=b//10
            ls+=[s]
        asc=shift(ls,k)
        j=1
        for i in asc:
            buf+=i*j
            j*=10
        res += str(buf)
    return res

while 2:
    mes=input()
    print(hash(mes))