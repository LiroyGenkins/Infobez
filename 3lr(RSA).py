import math
import random
import sympy as sy

n = int(input("Введите длинну чисел q и p в битах: "))
q = sy.randprime(2**(n-1),2**n)
p = sy.randprime(2 ** (n - 1), 2 ** n)
while(q==p):
    p = sy.randprime(2 ** (n - 1), 2 ** n)
print("q: ",q,"\np: ",p)
n=p*q
print("Открытый ключ n: ",n)
Euler=(q-1)*(p-1)
print("Функция Элера Ф(n): ", Euler)
e=sy.randprime(3,20)
while(math.gcd(e,Euler)!=1):
    e = sy.randprime(3, 30)
print("Открытая экспонента e: ",e)
k=1
d=(k*Euler+1)/e
while(d%1!=0):
    k+=1
    d=(k*Euler+1)/e
d=int(d)
print("Секретный ключ d: ", d,"\nАлиса отправляет e и n Бобу")
mes=random.randint(0,n-1)
print("Секреетное сообщение Боба: ",mes)
c=(mes**e)%n
print("Зашифрованный текст c: ",c)
M=(c**d)%n
print("Дешифрованное сообщение M: ",M)



