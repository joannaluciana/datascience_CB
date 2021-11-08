# #normalna funkcja
# def simple_function():
#     print('Hello world!')
#     print('Wikipedia')
#
#
# simple_function()
#
# #dwa argumenty
# def myfunction(a,b):
#   return a+b
#
#
# print(myfunction(3,5))
#
#
# #dokumentacja opis we funkcji
# def my_function():
#     """Dokumentacja funkcji"""
#
# help(my_function)
#
# #kroliki rekurencja :D - Fibonacci
#
# #1para - 1ms - 1 para  2 pary - 1 msc - 2 pary 3 pary
#
# #fibonacii
#
# def fibbonaci_numbers(n):
#     ''' zwraca liczby Fibonacciego mniejsze od n '''
#     wynik = []
#     a, b = 0, 1
#     while a < n:
#         # while len(wynik) < n:
#         wynik.append(a)
#         a, b = b, a + b
#     return wynik
#
#
#
#
#
# x = fibbonaci_numbers(10)
# print(x)
# print(fibbonaci_numbers.__doc__)
#
# #dl lancucha o ogniwie
# def chain_length(c, d):
#     e=c * d
#     return e
#
# #dl lancucha znakow
# def string_length(l):
#     length=0
#     for letter in l:
#         length+=1
#
#     return length
#
# print(chain_length(8,2))
#
# print(string_length('kocha'))
#
# #sumowanie listy elementow
# def sum_list(l):
#     sum=0
#     for n in l:
#         sum +=n
#     return sum
#
#
# print('wynik sumy listy to: ' + str(sum_list([1,2,3,4])))
#
#
# #mnozenie listy elementow
# def mno_list(li):
#
#     wynik = li[0]
#     for el in li[1:]:
#         wynik*=el
#
#     return wynik
#
#
#
# print('wynik mno listy to: ' + str(mno_list([1,2,3,4])))
#
# #max
# def max_li(l):
#     n_max = l[0]
#
#     for el in l[1:]:
#         if el > n_max:
#             n_max = el
#
#     return n_max
#
# print('wynik max: ' + str(max_li([1,5,3,4,99,80])))
#
# # min
# def min_li(l):
#     n_min = l[0]
#
#     for el in l[1:]:
#         if el < n_min:
#             n_min = el
#
#     return n_min
#
# print('wynik min: ' + str(min_li([0,1,5,3,4,99,80])))
#
# # zliczanie znakow
#
# def num_chars(li):
#     dict = {}
#
#     for l in li:
#         list_keys = dict.keys()
#         print(list_keys)
#         if l in list_keys:
#             dict[l]+=1
#         else:
#             dict[l]=1
#     return dict
#
#
# print(num_chars('google'))
#
# # Napisz funkcję w Pythonie, który zlicza ciągi znaków, w których długość ciągu wynosi 2 lub więcej, a pierwszy i ostatni znak są takie same z podanej listy ciągów.
# # Przykładowa lista : ['abc', 'xyz', 'aba', '1221']
# # Oczekiwany wynik: 2
#
# def str_length (list):
#     sum=0
#     for el in list:
#         if len(el) >= 2 and el[0]==el[-1]:
#             sum += 1
#     return sum
#
# print(str_length(['abc', 'xyz', 'aba', '1221']))
#
#
# # Napisz funkcję w Pythonie, aby uzyskać listę posortowaną w porządku rosnącym według ostatniego elementu w każdej krotce z podanej listy niepustych krotek.
# # Przykładowa lista: [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# # Oczekiwany wynik : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
#
# li = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
#
# def sec_krot(krot):
#     return krot[-1]
#
# def sort_krot(li):
#
#     return sorted(li, key=sec_krot(krot) )
#
#
# print(sort_krot(li))


# Napisz funkcję w Pythonie, aby uzyskać łańcuch składający się z pierwszych 2 i ostatnich 2 znaków z danego łańcucha. Jeśli długość ciągu jest mniejsza niż 2, zwróć zamiast tego pusty ciąg.
# Przykładowy ciąg : Python
# Oczekiwany wynik: Pyon
# Przykładowy ciąg : Py
# Oczekiwany wynik: PyPy
# Przykładowy ciąg : P
# Oczekiwany wynik: pusty ciąg


def string_con(st):

    if len(st) < 2:
        return ""
    return st[:2] + st[-2:]

print(string_con("python"))


#silnia - rekurencyjnie
def power_num(n):

    while n>1:
        return power_num(n-1)*n
    return 1

print(power_num(9))

#Fibonacci - rekurencyjnie

def fibonacci(n):
    if n < 1:
        return 0
    if n < 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(7))
print('------------------------------------------------------------')
for i in range(10):
    print(fibonacci(i))
