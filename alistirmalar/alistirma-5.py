# -*- coding: utf-8 -*-
from core import yardimcilar as helpers


tahmin_edilen_sayi = helpers.sayi_tahmin_et()

# kullanidan bir sayi aliyoruz
girilen_sayi = -1

deneme_sayisi = 0

while girilen_sayi != tahmin_edilen_sayi:

    deneme_sayisi += 1

    helpers = int(raw_input("Bir sayi tahmin edin: "))

    if girilen_sayi < tahmin_edilen_sayi:
        helpers.yazdir("küçük girdiniz, arttirin")

    elif girilen_sayi > tahmin_edilen_sayi:
        helpers.yazdir("büyük girdiniz, azaltın")

    else:
        helpers.yazdir("bingo! doğru tahmin. %s. denemede bildiniz" % deneme_sayisi)


