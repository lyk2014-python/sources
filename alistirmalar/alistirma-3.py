def kare(r):
    return r * r

def cember_hesapla(r):
    pi = 3.14
    return (pi * kare(r))

def yazdir(mesaj):
    print "-" * 30
    print mesaj
    print "-" * 30


print "Cemberin yari capi?",

r = raw_input()

r = int(r)

yazdir("Cemberin alani: %d" % cember_hesapla(r))
