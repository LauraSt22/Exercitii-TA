#Exercitiul 1
# variabila = parte din memoria unui calculator in care se stocheaza diferite date

#Exercitiul 2

# am declarat si initializat
# variabila string
prenume = 'Laura'

# variabila integer
varsta = 26

# variabila float
inaltime = 1.65

# variabila boolean
gen_feminin = True

#Exercitiul 3
print(type(prenume))
print(type(varsta))
print(type(inaltime))
print(type(gen_feminin))

#Exercitiul 4
print(round(inaltime))
inaltime = 2
print(type(inaltime))

#Exercitiul 5
print(f'Ma numesc : {prenume}')
print(f'Am varsta de : {varsta}')
print(f'Am inaltimea de : {inaltime}')
print(f'Sunt femeie, deci sunt de gen feminin: {gen_feminin}')

#Exercitiul 6
nume = input('Alege un nume')
prenume = input('Alege un prenume')
a = (nume + ' ' + prenume)
print(a)
print(len(a))
lungime_a = 13
print(f'Numele complet are {lungime_a} caractere')

#Exercitiul 7
lungimea = int(input('Alege lungimea'))
latimea = int(input('Alege latimea'))
x = lungimea*latimea
print(f'Aria dreptunghiului este {x}')

#Exercitiul 8
str = 'Coral is either the stupidest animal or the smartest rock'
print(str.count(" the ")) #afiseaza de cate ori apare 'the' in str

#Exercitiul 9
str = 'Coral is either the stupidest animal or the smartest rock'
str1 = str.replace(' the ', ' THE ')
print(str1)

#Exercitiul 10
str = 'Coral is either the stupidest animal or the smartest rock'
var = str.isdigit()
print(var)
assert str != var
print('str nu contine doar numere, contine litere')

#Optionale - Exrcitiul 11
str = input('Adauga un cuvant de dimensiune impara: ')
print(len(str))
print(str[-5]) #afiseaza litera din mijloc

#Exercitiul 12
str = 'abcdcba'
print(str)
print(str[::-1])
if str == str[::-1]:
    print('Stringul este palindrom')
else:
    print('Stringul nu este palindrom')
assert str == str[::-1]

#Exercitiul 13
a = input('')
print(a)
var1 = 'alabala'
var2 = 'portocala'
print(var1, var2)

#Exercitiul 14
x = input('')
lista = x.split()
print(lista)
x1 = (x[0]) # afisam prima litera a lui x
print(x1)
litera_mare = x[1:-1].replace('a', 'A')
print(x1 + litera_mare + x1)

#Exercitiul 15
a = input('Introduceti user')
b = input('Introduceti parola')
lungime_b = (len(b))
passw = str(lungime_b * '*')
print(f'Parola pentru user {a} este {passw} si are {lungime_b} caractere')
