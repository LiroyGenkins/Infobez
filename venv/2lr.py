import random

class Person():
    def __init__(self,g,p):
        self.g=g
        self.p=p
        self.public_num=0
        self.self_pow=0
        self.key=0
        self.foreign_num = 0
        self.foreigh_pow = 0

    def gen_public_num(self):pass
    def send(self, Person):pass
    def gen_key(self):pass

class Alice(Person):
    def gen_public_num(self):
        self.self_pow = random.randint(0,20000)
        self.public_num = int(self.g**self.self_pow)%self.p

    def send(self, other):
        other.foreign_num=self.public_num

    def gen_key(self):
        self.key=int(self.foreign_num**self.self_pow)
        self.key %= self.p

class Bob(Person):
    def gen_public_num(self):
        self.self_pow = random.randint(0, 20000)
        self.public_num = int(self.g ** self.self_pow) % self.p

    def send(self, other):
        other.foreign_num = self.public_num

    def gen_key(self):
        self.key = int(self.foreign_num ** self.self_pow)
        self.key %= self.p

def D_H(g,p):
        alice = Alice(g,p)
        bob = Bob(g,p)
        alice.gen_public_num()
        print(f"Alice generate privat pow: {alice.self_pow}")
        print(f"Alice generate public number: {alice.public_num}")
        alice.send(bob)
        print(f"Alice sent it to Bob, Bob's part of key: {bob.foreign_num}")
        bob.gen_public_num()
        print(f"Bob generate privat pow: {bob.self_pow}")
        print(f"Bob generate public number: {bob.public_num}")
        bob.send(alice)
        print(f"Bob sent it to Alice, Alice's part of key: {alice.foreign_num}")

        alice.gen_key()
        bob.gen_key()
        print(f"Alice generate key: {alice.key}")
        print(f"Bob generate key': {bob.key}")

g = random.randint(0, 1000000)
p = random.randint(0, 1000000)

print(f"g: {g}, p: {p}")
D_H(g,p)