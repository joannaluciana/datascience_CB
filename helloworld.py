i=12
f=12.000122323232
b = 2.71828 > 3
print(type(b))
print(b)
zmienna = 127
print(zmienna)

sampleStr="Datatypes"
middleIndex = int(len(sampleStr) / 2)
print("Oryginalny ciąg to", sampleStr)
middleThree = sampleStr[middleIndex - 1:middleIndex + 2]
print("To są trzy środkowe znaki", middleThree)


# Biorąc pod uwagę 2 ciągi, s1 i s2 zwróć nowy ciąg złożony z pierwszego, środkowego i ostatniego znaku każdego ciągu wejściowego
# Dane:
# s1 = "America"
# s2 = "Japan"
# Oczekiwany wynik:
# AJrpan

s1 = "America"
s2 = "Japan"

mid1= int(len(s1)/2)
mid2= int(len(s2)/2)
finalString = s1[0] + s2[0] + s1[mid1] +  s2[mid2] +  s1[-1] + s2[-1]

print(finalString)

print(s1[::-1])

lista = [1, 2, 3, 4, -5, 6, -10]






print(lista)

print(type(lista))

liczby = [0.1, 0.2, 0.3, 4.5, -7.3, 6.87, 10]

print(liczby)

print(type(liczby))

lista = [1, "Berta", 3, 4, -5, "kot", -10.75, 3.14]

print(lista[1:6])

print(lista[2:6:2])

print(lista[:4])

print(lista[:3])

print(lista[-2:])

print(lista[-4:-1])

#cala i od tylu
print(lista[::-1])

print(lista[:])

lista = [1, "Berta", 3, 4, -5, "kot", -10.75, 3.14]



print(lista)

lista = [2, 3, 5, 7, 9]

print(lista)


lista[2:4] = ["pies", "a", "2"]

print(lista)

lista = [1, "Berta", 3, 4, -5, "kot", -10.75, 3.14]

lista.insert(2,"zebra")

print("lista")

imiona = ["Anastazja", "Tomasz" , "Magdalena", "Michał", "Paweł", "Paweł", "Elżbieta", "Joanna", "Michał", "Łukasz", "Kamil", "Marcin", "Jakub", "Natalia"]
imiona2 = sorted(imiona)
print(imiona2)


#slwonik
slownik =  { "ala": "kot", "ola": 1 , "brainer": True}

print(slownik)

tel = {} # pusty słownik

print(tel)

tel = {'Maja': 500456 , 'Jasio': 343455}

print(tel)

tel['Ola'] = 3024127

print(tel)

del tel['Maja']

print(tel)

#tworzenie slownika
tel = dict([('Jan', 4139277), ('Kazimierz', 4126327)])
print(tel)
c = {x: x**2 for x in (2, 4, 6)}  # {2: 4, 4: 16, 6: 36}
print(c)

x = False
if not x :
    print("warunek spełniony")
else:
    print("warunek niespełniony")

niepusta_wartosc = 0 or 0.0 or "" or [] or "test" or  [123]

kazda_wartosc = "test" and [123]

"test" or 0

# Odwróć wynik, zwróć False, jeśli wynik jest prawdziwy
# nie ( x > 3 i x < 10 )
# Spróbuj!

nice = True
personality = ("wredny", "miły")[nice]
print("Kot jest", personality)  # Wyjście: Kot jest miły

string = 'Python'

# Pętla:
for litera in string:
    print('litera:', litera)

# Gdyby nie było pętli:
# litera = string[0]
# print('litera:', litera)
# litera = string[1]
# print('litera:', litera)
# litera = string[2]
# print('litera:', litera)
# litera = string[3]
# print('litera:', litera)
# litera = string[4]
# print('litera:', litera)
# litera = string[5]
# print('litera:', litera)

warzywa = ['marchew', 'kalafior', 'kapusta']
for warzywo in warzywa:
    print('warzywo:', warzywo)

kursanci = ['Anastazja',
            'Tomasz',
            'Magdalena',
            'Michał',
            'Paweł',
            'Paweł',
            'Elżbieta',
            'Joanna',
            'Michał',
            'Łukasz',
            'Kamil',
            'Marcin',
            'Jakub',
            'Natalia']

kursanci.sort()
kobieta=0
for kursant in kursanci:
    if kursant[-1] =='a':
        print('kobieta ' + kursant + ' ' + str(kobieta + 1))
        kobieta +=1
print(kobieta)

print("Przykład range() w Pythonie")
print("Uzyskaj liczby z zakresu od 0 do 5")
for i in range(6):
    print(i, end=', ')

for i in range(5):
    print(i)
else:
    print('gotowe')

lines = list()
print('Wprowadź tekst po linijce.')
print('Żeby zakończyć wprowadź pustą linię.')
line = input('Następna linijka: ')
while line != '':
    lines.append(line)
    line = input('Następna linijka: ')  # reset
print(lines)

for n in range(2, 100):
    for x in range(2, n):
        if n % x == 0:
            break
    else: # normalny koniec pętli
        print(n, 'jest liczbą pierwszą')

    for num in range(1, 20):
        if not num % 2:  # num % 2 == 0
            print('Kolejna liczba parzysta:', num)
            continue
        print('Kolejna liczba:', num)

# Napisz program, który policzy największy wspólny dzielnik dwóch liczb podanych przez użytkownika
# W tym celu użyj operatora % oraz pętli for

l1 = int(input('Podaj liczbę 1: '))
l2 = int(input('Podaj liczbę 2: '))

l_max = max(l1, l2)
l_min = min(l1, l2)
# print(l_max)


for num in range(l_min, 0, -1):
    if l1 % num == 0 and l2 % num == 0:
        print(num)
        break


#zastepieni wartosci
a = "Code Brainers"
b = 317
print("a: {}, b: {}".format(a,b))
b, a = a, b
print("a: {}, b: {}".format(a,b))