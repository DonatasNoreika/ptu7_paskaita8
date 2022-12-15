
class Automobilis:
    def __init__(self, metai, modelis, kuro_tipas):
        self.metai = metai
        self.modelis = modelis
        self.kuro_tipas = kuro_tipas
        # print(self.metai, self.modelis, self.kuro_tipas)
        print(self.__str__())

    def vaziuoti(self):
        print("Važiuoja")

    def stoveti(self):
        print("Priparkuota")

    def pildyti_degalu(self):
        print("Degalai įpilti")

    def __str__(self):
        return f"{self.metai} {self.modelis}, {self.kuro_tipas}"


class Elektromobilis(Automobilis):
    def pildyti_degalu(self):
        print("Baterija įkrauta")

    def vaziuoti_autonomiskai(self):
        print("Važiuoja autonomiškai")


automobilis1 = Automobilis(2019, "Toyota Corolla", 'hibridas')
automobilis2 = Elektromobilis(2022, "Tesla Model S Plaid", 'elektra')

print(automobilis1)
automobilis1.stoveti()
automobilis1.vaziuoti()
automobilis1.pildyti_degalu()
automobilis2.stoveti()
automobilis2.vaziuoti()
automobilis2.pildyti_degalu()
automobilis2.vaziuoti_autonomiskai()
