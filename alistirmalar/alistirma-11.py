class Insan(object):
    def __init__(self, isim, soy_isim, boy, yas, kilo):
        self.isim = isim
        self.soy_isim = soy_isim
        self.boy = boy
        self.yas = yas
        self.kilo = kilo
        self.mesaj_kutusu = []

    def kimlik_bas(self):
        print "benim adim: %s, soyadim ise: %s" % (self.isim, self.soy_isim)

    def __str__(self):
        return "%s %s" % (self.isim, self.soy_isim)

    def mesajlari_goster(self):
        for mesaj in self.mesaj_kutusu:
            print '-------------------------------'
            print mesaj


class Ogrenci(Insan):

    def __init__(self, isim, soy_isim, boy, yas, kilo, okul, sinif, veli):
        super(Ogrenci, self).__init__(isim, soy_isim, boy, yas, kilo)
        self.okul = okul
        self.sinif = sinif
        self.veli = veli
        self.kaldigi_dersler = []
        self.gectigi_dersler = []

    def egitim_bas(self):
        print "Gectigim dersler: %s" % ','.join(self.gectigi_dersler)
        print "Kaldigim dersler: %s" % ','.join(self.kaldigi_dersler)

class Ogretmen(Insan):

    def __init__(self, isim, soy_isim, boy, yas, kilo, verdigi_ders):
        super(Ogretmen, self).__init__(isim, soy_isim, boy, yas, kilo)
        self.verdigi_ders = verdigi_ders

    def ders_birak(self, ogrenci):
        ogrenci.kaldigi_dersler.append(self.verdigi_ders)

        telgraf = Telgraf(self, ogrenci.veli,
                          "%s %s dersinden kaldi, haberiniz olsun" % (
                              ogrenci.isim, self.verdigi_ders))

        telgraf.gonder()

    def ders_gecir(self, ogrenci):
        ogrenci.gectigi_dersler.append(self.verdigi_ders)


class Telgraf(object):

    def __init__(self, kimden, kime, mesaj):
        self.kimden = kimden
        self.kime = kime
        self.mesaj = mesaj

    def gonder(self):
        self.kime.mesaj_kutusu.append('%s diyor ki: %s' % (self.kimden.isim,
                                                           self.mesaj))


alinin_babasi = Insan("emre", "alptekin", 190, 50, 70)
ali = Ogrenci("ali", "alptekin", 172, 21, 70, "KTU", "9A2", alinin_babasi)
aysenin_babasi = Insan("kamil", "yildiz", 190, 50, 70)
ayse = Ogrenci("ayse", "yildiz", 172, 21, 70, "KTU", "10A2", aysenin_babasi)

mahmut_hoca = Ogretmen("mahmut", "hoca", 190, 70, 10, "Edebiyat")
riza_hoca = Ogretmen("riza", "hoca", 190, 70, 10, "Bilgisayar")
turgut_hoca = Ogretmen("turgut", "hoca", 190, 70, 10, "Fizik")
kamil_hoca = Ogretmen("kamil", "hoca", 190, 70, 10, "Matematik")

mahmut_hoca.ders_gecir(ayse)
riza_hoca.ders_birak(ayse)
turgut_hoca.ders_birak(ayse)
kamil_hoca.ders_birak(ayse)

ayse.egitim_bas()

aysenin_babasi.mesajlari_goster()