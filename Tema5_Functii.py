#Exercitiul 1
def suma(a, b):
     return(a+b)
print(suma(19,10))

#Exercitiul 2
def num(a):
    if a%2 == 0:
        return True
    else:
        return False
print(num(5))
print(num(6))

#Exercitiul 3
def count_ch(nume, prenume):
    nume_complet = nume + ' ' + prenume
    value = 0
    for i in nume_complet:
        value = value+1
    return value
print(f'Numarul total de caractere din numele complet este: ',count_ch('Stanciu', 'Laura'))

#Exercitiul 4
def arie_dreptunghi(a,b):
    return a*b
print(f'Aria dreptunghiului este {arie_dreptunghi(7,5)}')

#Exercitiul 5
def arie_cerc(pi, R):
    return (3.14 * 3**2)
print(f'Aria cercului este {arie_cerc(3.14, 3)}')

#Exercitiul 6
def check(c):
    str= 'calculator'
    if c in str:
        return True
    else:
        return False

print(check('l'))

#Exercitiul 7
def nr_de_caractere(s):
    d={'upper_case':0, 'lower_case':0}
    for c in s:
        if c.isupper():
            d['upper_case'] +=1
        elif c.islower():
            d['lower_case'] +=1
    print(f'Numarul de upper cases este: ',d['upper_case'] )
    print(f'Numarul de lower cases este: ', d['lower_case'])

print(nr_de_caractere(f'Numarul Total DE CaracterE mici este '))

#Exercitiul 8
def func(a):
    return [abs(n) for n in a]

print(func(a = [1, -2, 5, -9, 10, 20,34, -4]))

#Exercitiul 9
def numbers(x,y):

    if x > y:
        print(f'Numarul {x} este mai mare decat numarul {y}')
    elif x < y:
        print(f'Numarul {y} este mai mare decat numarul {x}')
    else:
        print(f'Numerele sunt egale.')

print(numbers(10, 5))
print(numbers(5, 5))
print(numbers(9, 11))

#Exercitiul 10
def func(x, set={}):
    if x == 8:
        set.add(8)
        print(f'Am adaugat numarul {x} in set.')
        return True
    else:
        print(f'Nu am adaugat numarul {x} in set. Acesta exista deja.')
        return False

print(func(8, set={7, 6, 2, 12}))
print(func(7, set={7, 6, 8, 2, 12}))

#Optional - Exercitiul 11
from calendar import monthrange
num_days = monthrange(2022, 10)[1]
print(num_days)


from calendar import monthrange
def numar_zile_intr_o_luna(an=2022, luna=8):
    return monthrange(an, luna)[1]
print(numar_zile_intr_o_luna(2022, 8))

#Exercitiul 12
def calculator(a,b):
    suma=a+b
    diferenta=a-b
    inmultirea=a*b
    impartirea=a/b
    return suma, diferenta, inmultirea, impartirea

a,b,c,d = calculator(10, 2)
print('Suma numerlor este: ', a)
print('Diferenta numerelor este: ', b)
print('Inmultirea numerelor este: ', c)
print('Impartirea numerelor este: ', d )

#Exercitiul 13
def frecventa_num(list):
    dict ={}
    list = [1,1,4,1,2,2,5,5,6,8,7,9,0,0,1,0,2,3]
    for i in list:
        dict[i] = dict.get(i, 0) +1
    return dict

print(frecventa_num(list))

#Exercitiul 14
def max(a,b,c):
    if (a>b) and (a>c):
        maximum = a
    elif (b>a) and (b>c):
        maximum = b
    else:
        maximum = c

    return maximum

a=80
b=20
c=170
print(f'Numarul cel mai mare este', max(a,b,c))

#Exercitiul 15
def sum(n):
    if n == 0:
        return 0
    else:
        return n + sum(n-1)
print(sum(3))


#Bonus - Exercitiul 16
def list(list1, list2):
    num_comune = []
    for x in list1:
        if x in list2:
            num_comune.append(x)
    return num_comune
print(f'Numerele comune dintre cele doua liste sunt: ', list(list1 = (1,2,3,4,5,10,20), list2 = (1,5,15,20,25,2)))

#Exercitiul 17
def pret_redus(a,b):

    if b >110:

        print('Reducerea este invalida, nu se poate aplica.')
    elif b <=100:

        print(f'Discountul este de ', int((a/100)*b), '$')
        print(f'Pretul este ', a - (a/100)*b, '$')


print(pret_redus(145,120))
print(pret_redus(145,10))
print(pret_redus(145,80))
print(pret_redus(145,130))
print(pret_redus(100,10))

#Exercitiul 18
import datetime
now = datetime.datetime.now()
print ("Data si ora curenta in Romania : ", now.strftime("%Y-%m-%d %H:%M:%S"))

from datetime import datetime
import pytz
now = datetime.utcnow()
tz=pytz.timezone('Asia/Shanghai')
tz1=pytz.timezone('America/New_York')
nowChina = tz.localize(now)
new=tz1.localize(now)
print(nowChina)
print(new) #printam si ora din America pentru a fi mai clara diferenta de ora
#China este cu 12 ore inaintea orei din New York si cu 8 ore inaintea orei din Romania

#Exercitiul 19
import datetime
prezent = datetime.date.today()
viitor = datetime.date(2022, 12, 25)
diff = viitor - prezent
print(f'Mai sunt {diff.days} pana la Craciun.')
