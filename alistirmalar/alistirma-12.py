from datetime import date

class Hesap(object):

    def __init__(self, isim, yas, bakiye=0):
        self.isim = isim
        self.yas = yas
        self.bakiye = bakiye
        self.islemler = []

    def transfer(self, kimden, miktar):
        kimden.para_yukle(miktar)
        self.bakiye -= miktar
        self.islemler.append(
            "%s tarihinde %s hesabina %s tl transfer edildi" % (
                date.today(), kimden.isim, miktar))

    def para_yukle(self, miktar):
        self.bakiye += miktar
        self.islemler.append("%s tarihinde %s tl yuklendi" % (
            date.today(), miktar))

    def para_cek(self, miktar):
        self.bakiye -= miktar
        self.islemler.append("%s tarihinde %s tl cekildi" % (
            date.today(), miktar))


fatih = Hesap("fatih", 21, 50)
halit = Hesap("halit", 21, 100)

print "Fatih'in bakiyesi:", fatih.bakiye
print "Halit'in bakiyesi:", halit.bakiye

fatih.transfer(halit, 25)

print "Fatih'in kalan bakiyesi:", fatih.bakiye
print "Halit'in toplam bakiyesi:", halit.bakiye

print '----------------'

for islem in fatih.islemler:
    print ' -', islem
