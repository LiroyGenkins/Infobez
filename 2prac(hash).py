#Сначала введённое сообщение разбивается на буквы, которые переводятся в численное значение по таблице ASCII,
#затем они переводятся в троичный код, после чего происходит циклический сдвиг каждой буквы на величину равную
#среднему арифметическому кодов всех букв в сообщении.
def shift(tx, step): #функция циклического сдвига
    if step < 0:
        step = abs(step)
        for i in range(step):
            tx.append(tx.pop(0))
    else:
        for i in range(step):
            tx.insert(0,tx.pop())
    return tx

def hash(st):
    res,c="",0
    for i in st:    #подсчёт среднего арифметического по кодам
        c+=ord(i)
    k=int(c/len(st))

    for i in st:    #обработка каждой буквы
        n = ord(i)
        ls, buf = [], 0
        b = 0
        j = 1
        while n:    #перевод в троичный код
            n, enc=divmod(n,3)
            b+=enc*j
            j *= 10
        while b:
            s=b%10
            b=b//10
            ls+=[s]
        asc=shift(ls,k)     #циклический сдвиг на среднее k
        j=1
        for i in asc:
            buf+=i*j
            j*=10
        res += str(buf)
    return res

while 2:
    mes=input()
    print(hash(mes))