# Typy wbudowane w pythona

# int - liczba całkowita (granice zależne od architektury) (w CPythonie - 64 bity - (2^63)-1 = 9,223,372,036,854,775,807)
# float - liczba zmiennoprzecinkowa (-1.7976931348623157e+308 do 1.7976931348623157e+308)
# bool - wartość logiczna (True / False)
# str - tekst (ciąg znaków)
# list - lista
# tuple - krotka
# dict - słownik
# set - zbiór

# Procedury pythona

# match - dopasowanie wzorca

# if/elif/else - warunek

# Operatory logiczne
# - == - operator porównania
# - != - operator różności
# - < - operator mniejsze niż
# - > - operator większe niż
# - <= - operator mniejsze lub równe
# - >= - operator
# - and - operator i
# - or - operator lub
# - not - operator negacji

# Operatory arytmetyczne
# - + - operator dodawania
# - - - operator odejmowania
# - * - operator mnożenia
# - / - operator dzielenia
# - // - operator dzielenia całkowitego
# - % - operator modulo
# - ** - operator potęgowania
# - divmod - funkcja zwracająca wynik dzielenia i resztę z dzielenia

reszta = 123 % 50
iloraz = 123 // 50
[reszta, iloraz] = divmod(123, 50)

counter = 5

if counter > 5:
    print("wartosc wieksza od 5")
elif counter == 5:
    print("wartosc równa 5")
else:
    print("wartosc mniejsza od 5")

# if <wyrazenie-warunkowe>:
#     <akcje>
# elif <wyrazenie-warunkowe>:
#     <akcje>
# else:
#     <akcje>

# while/break/continue - pętla nieskończona (warunkowa)

counter = 0
while counter < 10:
    counter += 1    
    print(f"Wartosc: {counter}")
    print("x")

    if counter > 5:
        continue

    print("y")

counter = 0
while counter < 10:
    counter += 1
    print(f"Wartosc: {counter}")

# for - pętla po kolekcji/iteratorze (lub warunkowa)

# range dziala na [start, end)

for i in range(-5, 10, 2):
    print(f"Wartosc: {i}")

# index: 0         1  2  3  4  5  6  7
lista = ["adam 3", 8, 4, 7, 2, 3, 9, 8]

print(lista)
for index, numer in enumerate(lista):
    if numer == "adam 3":
        lista[index] = 0
    # czy jestesmy w stanie wykonac ponizsze?

    # podmien kazda wartosc rowna 3 na 0
    pass
print(lista)

#  -7 -6 -5 -4 -3 -2 -1
#  0  1  2  3  4  5  6
# [8, 1, 7, 3, 4, 9, 8]

# co 2 element od 1 do 5 (wlacznie)
lis = lista[1:6:2]
print(lis)

for index, numer in enumerate(lista):
    print(f"Wartosc: {numer}, na indeksie: {index}")
    # Wartosc: 3, na indeksie: 0
    # Wartosc: 8, na indeksie: 1
    # Wartosc: 4, na indeksie: 2
    # Wartosc: 7, na indeksie: 3
    # Wartosc: 2, na indeksie: 4
    # Wartosc: 3, na indeksie: 5
    # Wartosc: 9, na indeksie: 6
    # Wartosc: 8, na indeksie: 7

# for <zmienna> in <kolekcja/iterator>:

# with - asercja zasobu

# try/except/finally - obsługa wyjątków
