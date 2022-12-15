import datetime

class Darbuotojas:
    def __init__(self, vardas, ikainis, dirba_nuo):
        self.vardas = vardas
        self.ikainis = ikainis
        self.dirba_nuo = datetime.datetime.strptime(dirba_nuo, "%Y-%m-%d")

    def _gauti_dienas(self):
        skirtumas = datetime.datetime.today() - self.dirba_nuo
        return skirtumas.days

    def paskaiciuoti_atlyginima(self):
        return self._gauti_dienas() * 8 * self.ikainis


class NormalusDarbuotojas(Darbuotojas):
    def _gauti_dienas(self):
        return super()._gauti_dienas() / 7 * 5


darbuotojas1 = Darbuotojas("Donatas", 100, "2019-02-05")
darbuotojas2 = NormalusDarbuotojas("Rokas", 100, "2019-02-05")
print(darbuotojas1.paskaiciuoti_atlyginima())
print(darbuotojas2.paskaiciuoti_atlyginima())
