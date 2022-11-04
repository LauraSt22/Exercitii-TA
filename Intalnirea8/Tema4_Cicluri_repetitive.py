#Exercitiul 1
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
for i in range(0, len(masini)): #parcurgere lista prin intermediul indexului
    print(f'Masina mea preferata este {masini[i]}')
for masina in masini: #for each
    print(f'Masina mea este {masina}')
while masini:
    print(f'Masina mea preferata este {masini.pop(0)}')

#Exercitiul 2
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
masini_majuscule = [s.lower() for s in masini[1:7]]
print(masini_majuscule)

#Exercitiul 3
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
for masina in masini:
    if masina == 'Mercedes':
        print('Am gasit masina dorita de dvs.')
        break
    else:
        print(f'Am gasit masina {masina}. Mai cautam.')

#Exercitiul 4
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
for masina in masini:
    if masina == 'Trabant':
        continue
    elif masina == 'Lastun':
        continue

    print(f'S-ar putea sa va placa masina {masina}')


#Exercitiul 5
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
masini_vechi = []
for masina in masini:
    if masina == 'Lastun':
        masini_vechi.insert(0, 'Lastun')
    elif masina == 'Trabant':
            masini_vechi.insert(1, 'Trabant', )

for i in range(len(masini)):
    if masini[i] == 'Lastun':
        masini[i] = 'Tesla'
    if masini[i] == 'Trabant':
        masini[i] = 'Tesla'
print(masini)
print(masini_vechi)

#Exercitiul 6
pret_masini = {'Dacia': 6800, 'Lastun': 500, 'Opel': 1100, 'Audi': 19000,'BMW': 23000}
print(pret_masini.keys())
preturi = pret_masini.values()
print(pret_masini)
x = pret_masini.items()
print(x)

for key, value in pret_masini.items():
    if value <= 15000:
        print(f'Pentru un buget sub 15000 puteti alege  masina {(key, value)} ')


#Exercitiul 7
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
x = numere.count(3)
for numar in numere:
    if numar == 3:
        print(f'Numarul 3 apare de {str(x)} ori')
        break


#Exercitiul 8
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
s = 0
for numar in numere:
    s = s + numar
print(f'Suma este {s}.')

#Exercitiul 9
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
max_num = 0
for i in numere:
    if i > max_num:
        max_num = i
print(max_num)

#Exercitiul 10
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
print(numere)
for i in range(len(numere)):
    numere[i] = -numere[i]
print(numere)

#Optional - Exercitiul 11
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
for i in alte_numere:
      if (i % 2 == 0):
         numere_pare.append(i)
      else:
         numere_impare.append(i)
print("Numere pare:", numere_pare)
print("Numere impare:", numere_impare)
for i in alte_numere:
    if i > 0:
        numere_pozitive.append(i)
    else:
        numere_negative.append(i)
print('Numere pozitive', numere_pozitive)
print('Numere negative', numere_negative)

#Exercitiul 12
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
lista_ordonata = []
while alte_numere:
    min = alte_numere[0]
    for x in alte_numere:
        if x < min:
            min = x
    lista_ordonata.append(min)
    alte_numere.remove(min)
print(lista_ordonata)


#Exercitiul 13
import random

numar_secret = random.randint(1, 30)
print(numar_secret)
numar_ghicit = []
numar = int(input('Alege un numar: '))
while numar < numar_secret:
    print('Numarul secret e mai mare')
    break
if numar > numar_secret:
    print('Numarul secret este mai mic.')

elif numar == numar_secret:
    print('Felicitari! Ai ghicit!')


#Exercitiul 14
randuri = int(input('Introduceti un numar: '))
for i in range(randuri+ 1):
    for j in range(i):
        print(i, end='')
    print('')

#Exercitiul 15
tastatura_telefon = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
  [0]
]
for row in tastatura_telefon:
    for col in row:
        print(f'Cifra curenta este', col)


