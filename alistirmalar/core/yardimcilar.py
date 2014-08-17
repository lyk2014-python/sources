import random


class Person(object):
    pass


PI = 3.14

def sayi_tahmin_et():
    return random.randint(0, 10)

def yazdir(mesaj):
    print "-" * 30
    print mesaj
    print "-" * 30

def kare(r):
    return r * r

def cember_hesapla(r):
    return (pi * kare(r))
