#Exercitiul 1
PI = 3.14
class Cerc:


    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare


    def descrie_cerc(self):
        print(f'Cercul are raza de {self.raza} cm ')
        print(f'si culoarea {self.culoare}')

    def arie_cerc(self):
        self.arie = PI * self.raza**2
        print(f'Aria cercului este: {self.arie}')

    def diametru_cerc(self):
        self.diametru = self.raza * 2
        print(f'Diametrul cercului este {self.diametru}')

    def circumferinta_cerc(self):
        print(f'Circumferinta cercului este {self.diametru * PI}')


cerc1 = Cerc(4, 'rosu')
cerc1.descrie_cerc()
cerc1.arie_cerc()
cerc1.diametru_cerc()
cerc1.circumferinta_cerc()


#Exercitiul 2
class Dreptunghi:
    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare


    def descrie(self):
        print(f'Dreptunghiul are lungimea {self.lungime}, latimea {self.latime} si culoarea {self.culoare}')

    def aria(self):
        print(f'Aria este', self.lungime * self.latime)

    def perimetru(self):
        print('Perimetrul este', 2*(self.lungime+self.latime))

    def schimba_culoarea(self, noua_culoare):
        self.culoare = noua_culoare


d = Dreptunghi(5, 6, 'rosu')
d.descrie()
d.aria()
d.perimetru()
d.schimba_culoarea('gri')
d.descrie()


# Exercitiul 3
class Angajat:


    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    def descrie(self):
        print(f'Nume: {self.nume}')
        print(f'Prenume: {self.prenume}')
        print(f'Salariu: {self.salariu}')
        print(f'Numele angajatului este: {self.nume} {self.prenume} si are salariul: {self.salariu}')

    def nume_complet(self):
        print(f'Numele complet al angajatului este: {self.nume} {self.prenume}')

    def salariu_lunar(self):
        print(f'Salariul lunar este: {self.salariu}')

    def salariu_anual(self):
        print(f'Salariul anual este: {self.salariu * 12} ')

    def marire_salariu(self, procent):
        self.procent = procent
        self.salariu = int((self.procent/100 * self.salariu) + self.salariu)
        print(f'Salariul lunar dupa marire este : {self.salariu}')

angajat1 = Angajat('Stanciu', 'Laura', 700)

angajat1.descrie()
angajat1.nume_complet()
angajat1.salariu_lunar()
angajat1.salariu_anual()
angajat1.marire_salariu(40)
angajat1.descrie()
angajat1.salariu_anual()


#Exercitiul 4

class Cont:


    def __init__(self, iban, titular_cont, sold):
        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = sold

    def afisare_sold(self):
        print(f'Titularul {self.titular_cont} are in contul IBAN {self.iban} suma de {self.sold} lei.')

    def debitare_cont(self, suma):
        self.suma = suma
        self.sold = self.sold + self.suma
        print(f'Dupa debitare, aveti in cont suma de {self.sold} lei.')

    def creditare_cont(self, suma):
        self.suma = suma
        if self.suma > self.sold:
            print(f'Fonduri insuficiente.')
        else:
            self.sold = self.sold - self.suma
            print(f'Contul a fost creditat cu suma de {self.suma} lei. Mai aveti disponibila suma de {self.sold} lei')

cont1 = Cont('ROBR0015129874562', 'Manea Ioana', 4000)

cont1.afisare_sold()
print( ' ' )
cont1.creditare_cont(500)
print(' ')
cont1.debitare_cont(800)
print(' ')
cont1.afisare_sold()


#Bonus - Exercitiul 5

from datetime import date
today = date.today()
print(today)
SERIA = 'FJ23'
from tabulate import tabulate
class Factura:


    def __init__(self, SERIA, numar, nume_produs, cantitate, pret_buc):
        self.numar = numar
        self.nume_produs = nume_produs
        self.cantitate = cantitate
        self.pret_buc = pret_buc

    def schimba_cantitatea(self, cantitate_noua):
        self.cantitate = cantitate_noua
        print(f'Noua cantitate este {cantitate_noua}')

    def schimba_pretul(self, pret_nou):
        self.pret_buc = pret_nou
        print(f'Noul pret este {pret_nou}')

    def schimba_nume_produs(self, nume_nou):
        self.nume_produs = nume_nou
        print(f'Noul nume este {nume_nou}')

    def genereaza_factura(self):
        from datetime import date
        today = date.today()
        print(f'Factura cu seria {SERIA} si numarul {self.numar} din data {today} ')
        print(tabulate([[SERIA, self.numar, today, self.nume_produs, self.cantitate, self.pret_buc, self.pret_buc*self.cantitate]], headers=['Seria', 'Numar', 'Data', "Nume Produs", "Cantitate", "Pret", "Total"], tablefmt="github"))


factura1 = Factura(SERIA, 11, 'Samsung', 3, 300)
factura1.schimba_nume_produs('Lenovo')
factura1.schimba_cantitatea(6)
factura1.schimba_pretul(350)
factura1.genereaza_factura()



#Exercitiul 6

class Masina:

    marca = 'Logan'
    culoare = 'gri'
    viteza_actuala = 0
    inmatriculata = False
    culori_disponibile = {'rosu', 'galben', 'albastru', 'roz', 'verde'}

    def __init__(self, model, viteza_maxima):
        self.model = model
        self.viteza_maxima = viteza_maxima

    def descrie(self):
        print(f'Marca masina: {self.model}')
        print(f'Culoarea masinii: {self.culoare}')
        print(f'Modelul masinii: {self.model}')
        print(f'Viteza masinii este {self.viteza_actuala}')
        print(f'Viteza maxima a masinii este {self.viteza_maxima}')
        if self.inmatriculata == False:
            print(f'Masina nu este inmatriculata.')
        else:
            print(f'Masina este inmatriculata.')


    def inmatriculare(self):
        if self.inmatriculata == False:
            self.inmatriculata = True
        else:
            print(f'Masina este deja inamtriculata.')

    def vopseste(self, culoare):
        if culoare in self.culori_disponibile:
            self.culoare = culoare
            print(f'Culoarea {culoare} inca mai este disponibila.')
        else:
            print(f'Culoarea {culoare} nu este disponibila.')

    def accelereaza(self, viteza):
        if viteza <= self.viteza_maxima and viteza>0:
            self.viteza_actuala = viteza
            print(f'Aveti viteza de {viteza}')
        elif viteza > self.viteza_maxima:
            self.viteza_actuala = self.viteza_maxima
            print(f'Nu puteti accelera mai mult de {self.viteza_maxima}')
        else:
            print(f'Viteza nu poate fi negativa.')

    def franeaza(self):
        self.viteza_actuala = 0
        print(f'Masina s-a oprit.')


masina1 = Masina('MCV', 260)

masina1.descrie()
print(' ')
masina1.inmatriculare()
masina1.descrie()
print(' ')
masina1.vopseste('rosu')
masina1.vopseste('negru')
print(' ')
masina1.accelereaza(180)
masina1.accelereaza(280)
print(' ')
masina1.franeaza()


#Exercitiul 7

class TodoList():

    todo = {

    }

    def adauga_task(self):
        self.todo['masina'] = 'Opreste masina!'
        self.todo['serviciu'] = 'Nu uita de sedinta!'
        self.todo['scoala'] = 'Ai examen!'

    def finalizeaza_task(self, nume):
        self.nume = nume
        if self.nume in self.todo:
            self.todo.pop(self.nume)
            print(f'Taskul {self.nume} a fost finalizat.')
        else:
            print(f'Taskul {self.nume} nu este in lista.')

    def afiseaza_todo_list(self):
        print(f'To do list: {self.todo.keys()}')

    def afiseaza_todo(self):
        for key, value in self.todo.items():
            print(key, ' : ', value)

#     def afiseaza_detalii_suplimentare(self, nume_task):
        self.nume_task = nume_task
        if nume_task not in self.todo:
            print(f'Taskul {self.nume_task} nu este in lista. Ati dori sa il adaugati?')
            self.raspuns = input(f'da sau nu')
            if self.raspuns == 'nu':
                print(f'La revedere!')
            else:
                self.detalii = input(f'Detaliile pentru noul task sunt: ')
                self.todo[nume_task] = self. detalii

todo = TodoList()
todo.afiseaza_todo_list()
todo.adauga_task()
todo.afiseaza_todo_list()
todo.finalizeaza_task('scoala')
todo.finalizeaza_task('dentist')
todo.afiseaza_todo_list()
todo.afiseaza_detalii_suplimentare('casa')
todo.afiseaza_todo()


