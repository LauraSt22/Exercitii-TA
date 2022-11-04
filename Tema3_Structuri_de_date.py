#Exercitiul 1

note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
print(note_muzicale)
note_muzicale = note_muzicale[::-1]
print(note_muzicale)
note_muzicale.reverse()
print(note_muzicale)

#Exercitiul 2
print(note_muzicale.count('do'))


#Exercitiul 3
list1 = [3, 1, 0, 2]
list2 = [6, 5, 4]
list = list1 + list2
print(list)
for x in list2:
    list1.append(x)
print(list1)
list1.extend(list2)
print(list1)

#Exercitiul 4
list1 = [3, 1, 0, 2]
list2 = [6, 5, 4]
list = list1 + list2
print(list)
list.sort()
print(list)
list.remove(0)
print(list)

#Exercitiul 5
list1 = [3, 1, 0, 2]
list2 = [6, 5, 4]
list = list1 + list2
print(list)
list = [3, 1, 0, 2, 6, 5, 4]
if list == [3, 1, 0, 2, 6, 5, 4]:
    print(f'Lista nu este goala.')
else:
    print(f'Lista este goala.')

#Exercitiul 6
list = list.clear()
print(list)

#Exercitiul 7
list1 = [3, 1, 0, 2]
list2 = [6, 5, 4]
list = list1 + list2
print(list)
list = list.clear()
print(list)
list = [3, 1, 0, 2, 6, 5, 4]
if list != [3, 1, 0, 2, 6, 5, 4]:
    print(f'Lista nu este goala.')
else:
    print(f'Lista este goala.')

#Exercitiul 8
dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
keys = dict1.keys()
print(keys)

#Exercitiul 9
y = dict1.values()
print(y)
a = dict1.get('Ana')
print(a)
b = dict1.get('Gigel')
print(b)
c = dict1.get('Dorel')
print(c)
print(f'Ana a luat nota {a}')
print(f'Gigel a luat nota {b}')
print(f'Dorel a luat nota {c}')

#Exercitiul 10
dict1['Dorel'] = 6
print(dict1)
c1 = dict1.get('Dorel')
print(c1)

#Exercitiul 11
dict1.pop('Gigel')
dict1['Ionica'] = '9'
print(dict1)

#Exercitiul 12
zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
zile_sapt.add('luni')
print(zile_sapt)

#Exercitiul 13
z = weekend.issubset(zile_sapt) #aflam daca weekend este subset in zile_sapt
print(z)
if z == True:
    print('Weekend este un subset al zilelor din săptămânii.')
else:
    print('Weekend nu este un subset al zilelor din săptămânii.')

#Exercitiul 14
diferenta = zile_sapt.difference(weekend)
print(diferenta)

#Exercitiul 15
intersectie = zile_sapt.intersection(weekend)
print(intersectie)

#Optional - Exercitiul 1

SCHIMBARI_MAX = 3
schimbari_ramase = SCHIMBARI_MAX
echipa  = {'j1', 'j2', 'j3', 'j4', 'j5'}
jucator_in = input('Introduceti un jucator care sa intre in teren')
jucator_out = input('Introduceti un jucator care sa iasa din teren')

if jucator_out in echipa and schimbari_ramase>0:
    if jucator_in in echipa:
        print('Nu putem face schimbarea')
    else:
        echipa.remove(jucator_out)
        echipa.add(jucator_in)
        schimbari_ramase = schimbari_ramase - 1
        print(f'Am introdus {jucator_in}')
        print(f'Am scos {jucator_out}')
        print(f'Echipa actuala este {echipa}')
        print(f'Mai avem {schimbari_ramase} schimbari')
else:
    if schimbari_ramase <=0:
        print(f'Nu mai avem schimbari')
    else:
        print(f'Nu putem face schimbarea pentru ca jucatorul {jucator_in} este deja in teren')