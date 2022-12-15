
class Irasas:
    def __init__(self, suma):
        self.suma = suma

class PajamuIrasas(Irasas):
    def __init__(self, suma, siuntejas, info):
        super().__init__(suma)
        self.siuntejas = siuntejas
        self.info = info

    def __str__(self):
        return f"Pajamos: {self.suma}, siuntėjas - {self.siuntejas}, info: {self.info}"

class IslaiduIrasas(Irasas):
    def __init__(self, suma, atsiskaitymo_budas, isigyta_preke_paslauga, info):
        super().__init__(suma)
        self.atsiskaitymo_budas = atsiskaitymo_budas
        self.isigyta_preke_paslauga = isigyta_preke_paslauga
        self.info = info

    def __str__(self):
        return f"Išlaidos: {self.suma}, atsiskaitymo būdas - {self.atsiskaitymo_budas}, įsigyta prekė/paslauga - {self.isigyta_preke_paslauga}, info: {self.info}"

class Biudzetas:
    def __init__(self):
        self.zurnalas = []

    def prideti_pajamu_irasa(self, suma, siuntejas, info):
        irasas = PajamuIrasas(suma, siuntejas, info)
        self.zurnalas.append(irasas)

    def prideti_islaidu_irasa(self, suma, atsiskaitymo_budas, isigyta_preke_paslauga, info):
        irasas = IslaiduIrasas(suma, atsiskaitymo_budas, isigyta_preke_paslauga, info)
        self.zurnalas.append(irasas)

    def gauti_balansa(self):
        bendrasuma = 0
        for irasas in self.zurnalas:
            if type(irasas) is PajamuIrasas:
                bendrasuma += irasas.suma
            if type(irasas) is IslaiduIrasas:
                bendrasuma -= irasas.suma
        return bendrasuma

    def gauti_ataskaita(self):
        for irasas in self.zurnalas:
            print(irasas)

biudzetas = Biudzetas()

while True:
    ivedimas = int(input("1 - įvesti pajamas\n2 - įvesti išlaidas\n3 - ataskaita\n4 - balansas\n0 - išeiti\n"))
    if ivedimas == 1:
        suma = float(input("Įveskite sumą: "))
        siuntejas = input("Įveskite siuntėją: ")
        info = input("Įveskite papildomą informaciją: ")
        biudzetas.prideti_pajamu_irasa(suma, siuntejas, info)
    if ivedimas == 2:
        suma = float(input("Įveskite sumą: "))
        atsiskaitymo_budas = input("Įveskite atsiskaitymo būdą: ")
        isigyta_preke_paslauga = input("Įsigyta prekė ar paslauga: ")
        info = input("Įveskite papildomą informaciją: ")
        biudzetas.prideti_islaidu_irasa(suma, atsiskaitymo_budas, isigyta_preke_paslauga, info)
    if ivedimas == 3:
        biudzetas.gauti_ataskaita()
    if ivedimas == 4:
        print("Balansas:", biudzetas.gauti_balansa())
    if ivedimas == 0:
        print("Viso gero")
        break