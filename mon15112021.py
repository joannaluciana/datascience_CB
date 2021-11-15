# import sys
# try:
#     f = open("plik.txt")
#     s = f.readline()
#     i = int(s.strip())  # Usuń spacje
#     print(i)
# except OSError as err:
#     print("Błąd systemu: {0}".format(err))
# except ValueError:
#     print("Nie można dokonać konwersji.")
# except:     # PEP 8: E722 nie używaj pustego 'except'
#     print("Nieoczekiwany wyjątek:", sys.exc_info()[0])
#     raise
#
# try:
#     print("Dzień dobry")
# except:
#     print("Coś poszło nie tak")
# else:
#     print("Nic nie poszło źle")
#
#
# try:
#     print("x")
# except:
#     print("Coś poszło nie tak")
# finally:
#     print("Klauzula „try except" jest zakończona")

#-----------------------------------------------------
#Typ własnego opisu błędu
# x = -1
#
# if x < 0:
#     raise Exception("Przepraszamy, brak liczb poniżej zera")
# --------------------------------------------------------------------------------------------
# Ćwiczenie 1
# Podczas pisania funkcji najlepiej jest przeprowadzić walidację liczb.
# Jeśli użytkownicy wprowadzą tekst, pojawi się błąd podczas próby konwersji na int.
# Napisz program, który poprosi użytkownika o podanie dwóch liczb.
# Dodaj i wydrukuj wynik.
# Jeśli nie zostanie wprowadzona liczba, zwróć komunikat o błędzie i poproś ponownie.



# while True:
#
#     try:
#         a = input("Podaj liczbe A")
#         b = input("Podaj liczbe B")
#         a = int(a)
#         b = int(b)
#         print(a+b)
#         break
#     except ValueError:
#
#         print("Wprowadz liczby")


# --------------------------------------------------------------------------------------------
# Ćwiczenie 2

# Ćwiczenie
# Podziel przez siebie dwie liczby
# Umieść:
# wynik = "Nie możesz podzielić przez 0"
# we właściwym miejscu, aby program uniknął ZeroDivisionError
# Podpowiedź 1: Po prostu umieść przypisanie wartości dla wyniku po linii Except
# Podpowiedź 2: Zwróć uwagę na wcięcia

# a = 5
# b = 0
# try:
#     wynik = a/b
# except ZeroDivisionError:
#     wynik = 'nie mozesz dzielic przez 0'
#
# print(wynik)

#  --------------------------------------------------------------------------------------------
# Ćwiczenie 3
# Napisz dowolny kod.
# Wychwyć w nim wyjątek, ale nic nie rób.

# a = 5
# b = 0
# try:
#     wynik = a/b
# except ZeroDivisionError:
#     pass

#  --------------------------------------------------------------------------------------------
# Ćwiczenie 4
# Spróbuj dodać int do ciągu.
# Umieść:
# msg = "Nie możesz dodać int do string"
# aby program uniknął błędu BaseException.
# Możesz użyć wyjątku Exception, chociaż zwykle powinno się ostrożnie używać tak potężnych instrukcji wyjątków.



# l= int(input("Podaj liczbe A"))
# s = input("Podaj String")
# msg = "Nie możesz dodać int do string"
#
# try:
#     l+ s
# except BaseException:
#     print(msg)

#  --------------------------------------------------------------------------------------------
# Ćwiczenie 5
# Stwórz trójelementową listę.
# Spróbuj wydrukować piąty element.
# Umieść:
# msg = "Jesteś poza zakresem listy"
# aby uniknąć wyjątku IndexError.

# a = [1,2,3]
# msg = "Jesteś poza zakresem listy"
#
# try:
#     print(a[4])
# except: IndexError :
#     print(msg )

#  --------------------------------------------------------------------------------------------
# Ćwiczenie 6

# Spróbuj otworzyć do czytania plik (podpowiedź: f = open(arg, "r")).
# W razie braku możliwości otwarcia pliku, obsłuż wyjątek.
# W przeciwnym przypadku wypisz:
# Nazwę pliku;
# Liczbę wierszy (podpowiedź: len(f.readlines()).
# Na koniec zamknij ten plik (podpowiedź: f.close()).

# arg = 'mon15112021.py'
#
# try:
#     f = open(arg, "r")
# except FileNotFoundError:
#     print('Nie mozna otworzyc pliku o nazwie ' + arg)
# else:
#     print('Plik o nazwie ' + arg + ' ma wierszy: ' + str(len(f.readlines())))
#     f.close()
#  --------------------------------------------------------------------------------------------
# Ćwiczenie 7
# Użyj finally do zamykania obiektów i czyszczenia zasobów.
# Spróbuj otworzyć i zapisać (podpowiedź: write) w pliku, którego nie można zapisać.
# Zapewnij, aby program mógł kontynuować bez pozostawiania otwartego obiektu pliku.
# import io
#
# try:
#     f = open('nowy-plik.txt', 'r')
#     f.write('dsdsdsdsdsdsdsd')
# except io.UnsupportedOperation:
#     print('nie da sie otworzyc pliku !')
# finally:
#     f.close()
#  --------------------------------------------------------------------------------------------
# Ćwiczenie 8
# Napisz funkcję dzielącą jej argument pierwszy przez drugi.
# Spróbuj wykonać działanie i zwrócić wynik.
# W przypadku błędu dzielenia przez zero, wypisz komunikat o błędzie.
# Wypisz komunikat, który zawsze się wypisze.
# Wywołaj funkcję z różnymi argumentami.


# def divided(a,b):
#
#
#     try:
#         wynik = a/b
#         return wynik
#     except ZeroDivisionError as err:
#         print('nie mozna dzielic przez 0')
#         print (err)
#     finally:
#         print('zawsze')
#
#
#
#
#
# a = int(input("Podaj liczbe A"))
# b = int(input("Podaj liczbe B"))
#
# print(divided(a,b))

# Ćwiczenie
# Użyj wszystkie 4 elementy struktury obsługi wyjątków przy otwieraniu plików.
# Spróbuj otworzyć do czytania plik.
# W razie braku możliwości otwarcia pliku, obsłuż wyjątek.
# W przeciwnym przypadku wypisz:
# Nazwę pliku;
# Liczbę wierszy.
# Na koniec zamknij ten plik.
# Jeżeli dany plik nie jest zamknięty (podpowiedź: f.closed), to go zamknij.

# arg = 'nowy-plik.txt'
#
#
#
# try:
#     f = open(arg)
# except IOError as a:
#     print('Nie mozna otworzyc pliku o nazwie ' + arg + ' IOError: ' + str(a))
#
# else:
#     print(arg + " " + str(len(f.readlines())))
# finally:
#     if not f.closed:
#         f.close()

# Otwórz plik
fo = open("text.txt", "r")
print("Nazwa pliku: ", fo.name)

line = fo.readline()
print("Czytaj linię: >" + line + "<")

# Ponownie ustaw wskaźnik na początek
fo.seek(0)
line = fo.readline()
print("Czytaj linię: >" + line + "<")

# Zamknij otwarty plik
fo.close()

