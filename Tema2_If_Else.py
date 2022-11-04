#Exercitiul 1
# conditionalul if...else evalueaza sintaxa daca este adevarata sau falsa. In functie de o conditie data, daca aceasta este adevarata atunci se va executa blocul cuprins de if, daca este falsa atunci se va executa blocul else.

#Exercitiul 2
x = input('Introduceti un numar')
y = int(x)
if y >= 0:
    print('X este numar natural')
else:
    print('X nu este numar  natural')

Introduceti un numar5
X este numar natural

Process finished with exit code 0

x = input('Introduceti un numar: ')
y = int(x)
if y >= 0:
    print('X este numar natural')
else:
    print('X nu este numar  natural')

#Exercitiul 3
x = input('Introduceti un numar: ')
y = int(x)
if y > 0:
    print('X este numar pozitiv.')
elif y < 0:
    print('X este numar negativ.')
else:
     print('X este numar neutru.')

#Exercitiul 4
x = input('Introduceti un numar: ')
a = int(x)
y = int(x)
if a >= -2 and x <=13:
    print('X este cuprins intre -2 si 13.')
else:
    print('X nu este cuprins intre -2 si 13.')

#Exercitiul 5
x = int(input('Introduceti un numar x: '))
y = int(input('Introduceti un numar y: '))
if (x-y) < 5:
    print('Diferenta dintre x si y este mai mica decat 5.')
else:
    print('Diferenta dintre x si y nu este mai mica decat 5.')

#Exercitiul 6
x = int(input('Introduceti un numar: '))
a = 5
b = 27
if not x == (a >= 5 and b <= 27):
    print('X nu se gaseste intre 5 si 27.')
else:
    print('X se gaseste intre 5 si 27.')

#Exercitiul 7
x = int(input('Introduceti un numar: '))
y = int(input("introduceti un numar: "))
if x ==  y:
    print('Numerele sunt egale.')
elif x > y:
    print('X este mai mare decat y.')
else:
    print('Y este mai mare decat x.')

#Exercitiul 8
x = int(input('Introduceti un numar: '))
y = int(input('Introduceti un numar: '))
z = int(input('Introduceti un numar: '))
if x == y == z:
    print('Triunghiul este echilateral')
elif x == y:
    print('Triunghiul este isoscel')
elif y == z:
    print('Triunghiul este isoscel')
elif x == z:
    print('Triunghiul este isoscel')
else:
    print('Triunghiul este oarecare')

#Exercitiul 9
x = str(input('Introduceti o litera: '))
if x == 'a':
    print( 'Litera aleasa este o vocala' )
elif x == 'e':
    print('Litera aleasa este o vocala')
elif x == 'i':
    print('Litera aleasa este o vocala')
elif x == 'o':
    print('Litera aleasa este o vocala')
elif x == 'u':
    print('Litera aleasa este o vocala')
else:
    print('Litera aleasa este o consoana')

#Exercitiul 10
nota = int(input('Introduceti o nota: '))
if nota == 9:
    print('Nota este A.')
elif nota == 10:
    print('Nota este A.')
elif nota == 8:
    print('Nota este B.')
elif nota == 7:
    print('Nota este C.')
elif nota == 6:
    print('Nota este D')
elif nota == 5:
    print('Nota este E.')
elif nota == 4:
    print('Nota este E.')
else:
    print('Nota este F.')

#Optional - Exercitiul 1
x = int(input('Introduceti un numar: '))
if x >= 4:
    print('Numarul ales are 4 cifre.')
else:
    print('Numarul ales nu are 4 cifre.')

#Exercitiul 2
x = int(input('Introduceti un numar: '))
if x == 6:
    print('Numarul ales are exact 6 cifre.')
else:
    print('Numarul ales nu are 6 cifre.')

#Exercitiul 3
x = int(input('Introduceti un numar: '))
if x % 2 == 0:
    print('Numarul ales este par.')
else:
    print('Numarul ales este impar.')

#Exercitiul 4
x = int(input('Introduceti un numar: '))
y = int(input('Introduceti un numar: '))
z = int(input('Introduceti un numar: '))
print(f'Numarul cel mai mare este', max(x, y, z))

if (x>y) and (x>z):
    print(f'{x} este numarul cel mai mare.')
elif (y>x) and (y>z):
    print(f'{y} este numarul cel mai mare.')
else:
    print(f'{z} este numarul cel mai mare.')

#Exercitiul 5
x = int(input('Introduceti valoarea unghiului: '))
y = int(input('Introduceti valoarea unghiului: '))
z = int(input('Introduceti valoarea unghiului: '))
if (x+y) > z:
    print('Triunghiul este valid.')
elif (x+z) > y:
    print('Triunghiul este valid.')
elif (y+z) > x:
    print('Triunghiul este valid.')
else:
    print('Triunghiul nu este valid.')

#Exercitiul 6
x = int(input('Introduceti un numar: '))
str = 'Coral is either the stupidest animal or the smartest rock'
print(str)
y = len(str)
print(y)
z = str.rstrip(' rock')
print(z)
a = int(y-x)
print(a)
if a == (y-x):
    print(z)
else:
    print('Numarul ales este invalid.')

#Exercitiul 7
str = 'Coral is either the stupidest animal or the smartest rock'
print(len(str))
a = str[:5]
print(a)
b = str[-4:]
print(b)
str_nou = (a) + (' ') + (b)
print(str_nou)
if str_nou == (a) + (' ') + (b):
    print('Coral rock')
else:
    print('Sintaxa gresita.')

#Exercitiul 8
str = 'Coral is either the stupidest animal or the smartest rock'
a = str[-4:]
print(a)
b = a.index('r')
print(b)
print(str[:-4])

#Exercitiul 9
str = input('Introduceti un cuvant: ')
print(len(str))
first = str[0]
print(first)
last = str[-1]
print(last)
if first.casefold() == last.casefold():
    print('Prima si ultima litera sunt la fel.')
else:
    print('Optiunea aleasa nu este valida.')

assert first.casefold() == last.casefold()

#Exercitiul 10
str = '0123456789'
a = len(str)
print(a)
y = str[0:10:2]
print(y)
x = str[1:10: 2]
print(x)

#Exercitii Bonus - Exercitiul 11
import random
random = random.randint(1, 6)
print(random)
dice_roll = int(input('Introduceti un numar: '))
if dice_roll == 0:
    print(f'Ai pierdut. Ai ales un numar mai mic. Ai ales {dice_roll} dar a fost {random} ')
elif dice_roll >= 7:
    print(f'Ai pierdut. Ai ales un numar mai mare. Ai ales {dice_roll} dar a fost {random} ')
else:
    print(f'Ai ghicit. Felicitari! Ai ales {dice_roll} si zarul a fost {random}')
