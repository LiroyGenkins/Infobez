import random

def Eratosphen(n):
    vec=[]
    for i in range(n+1):
        vec.append(True)
    p = 2
    pSr = 0
    for p in range(2,n//p,1):
        if vec[p]:
            for pSr in range(p*p,len(vec),1):
                if pSr%p == 0:
                    vec[pSr]=False
    return vec

class Person():
    def __init__(self,g,p):
        self._m_g=g
        self._m_p=p
        self._a=0
        self._b=0
        self._key=0
        self._A = 0
        self._B = 0

    def genNum(self):pass
    def send(self, Person):pass
    def genKey(self):pass

class Alice(Person):
    def genNum(self):
        size = 100000
        vec = Eratosphen(size)
        i = random.randint(0,size)
        while(vec[i]==False):
            i = random.randint(0,size)
        self._a = i
        self._A = int(self._m_g**self._a)%self._m_p

    def send(self, other):
        other._A=self._A

    def genKey(self):
        self.key=int(self._B**self._a)
        self.key %= self._m_p

class Bob(Person):
    def genNum(self):
        size = 100000
        vec = Eratosphen(size)
        i = random.randint(0, size)
        while (vec[i]==0):
            i = random.randint(0, size)
        self._b = i
        self._B = int(self._m_g ** self._B) % self._m_p

    def send(self, other):
        other._A = self._A

    def genKey(self):
        self.key = int(self._A ** self._b)
        self.key %= self._m_p

def D_H(g,p):
        alice = Alice(g,p)
        bob = Bob(g,p)
        alice.genNum()
        print(f"Alice generate a: {alice._a}")
        print(f"Alice generate A: {alice._A}")
        alice.send(bob)
        print(f"Bob's A': {bob._A}")
        bob.genNum()
        print(f"Bob generate b: {bob._b}")
        print(f"Bob generate B: {bob._B}")
        bob.send(alice)
        print(f"Alice's B': {alice._B}")

        alice.genKey()
        bob.genKey()
        print(f"Alice generate key: {alice.key}")
        print(f"Bob generate key': {bob.key}")

g = random.randint(0, 1000000)
p = random.randint(0, 1000000)

print(f"g: {g}, p: {p}")
D_H(g,p)