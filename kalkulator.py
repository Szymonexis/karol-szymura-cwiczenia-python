operacje = ['+', '-', '*', '/']

operacja_poprawna = False
while not operacja_poprawna:
    operacja = input(
        # ! powinnismy odrazu sprawdzic czy input zgadza sie z operacjami jakie posiadamy
        'Wpisz +,-,*,/ w zalezności od tego jaką chcesz wykonać operację:\n')

    if operacja in operacje:
        operacja_poprawna = True
    else:
        print("Podaj poprawna operacje!")

l = list()
lista_liczb = list()  # ! listy "latwiej" mozna tworzyc za pomoca `[]`
try:
    # ? dlaczego pierwsza liczba sie nie liczy???
    liczba = float(input('Jeśli chcesz wpisz kolejno liczby jakie zamierzasz uzyc w operacji pierwsza liczba się nie liczy i naciskaj enter jeśli wolisz wpisać liczby za pomocą oddzielania przecinka wpisz cokolwiek innego niz liczbę:\n'))
    while float('inf') > liczba > -float('inf'):
        liczba = float(
            input('Wpisz kolejno liczby jakie zamierzasz uzyc w operacji:\n'))
        if float('inf') > liczba > -float('inf'):
            l.append(liczba)
        else:
            continue
except:
    # ? wczesniej zbieralismy liczby jedna po drugiej, tutaj nagle zbieramy wszystkie?
    liczby = input(
        'Wpisz zbiór liczb oddzielając jedną od drugiej przecinkiem:')
    x = liczby.strip()
    c = x.split(',')
    for item in c:  # uzylem pomocy chatu, zeby mi wyjasnil jak zbudowac te funkcje,zeby dzialalo. chociaz dwa razy odpowiedzial zle i chcialem zeby udzielil mi odpowiedzi z petla for.
        #! uzywanie zagniezdzonych try-exceptow jest zlym pomyslem
        try:
            numbers = float(item.strip())
            l.append(numbers)
        except:
            continue
ilosc_elementow = len(l)
# print(ilosc_elementow)
# print(l)

#! to co sie dzieje wewnatrz if-ow jest dla mnie troche niezrozumiale
#! np. suma (mimo ze w pythonie `sum` sumuje wszystkie elementy w liscie) matematycznie powinna przyjmowac tylko dwa argumenty
if operacja == ('+'):  # tu uzywalem petli for i uzylem chatu do podpowiedzi, dlaczego wyskakuja mi tracebacki od godziny, okazalo się, ze da sie duzo prosciej xDD
    suma = sum(l)
    print('Suma: ', suma)
elif operacja == ('-'):  # tu chcialem poznac jak dzialaja inne rzeczy niz sum i okazalo sie, ze moje myslenie co do sumy bylo dobre xDDDD
    roznica = l[0]
    for liczba in l[1:]:
        roznica -= liczba
    print('Roznica: ', roznica)
elif operacja == ('*'):
    mnozenie = 1
    for mnoznik in l:
        mnozenie *= mnoznik
    print('Wynik mnozenia: ', mnozenie)
elif operacja == ('/'):
    #! nie tak dziala dzielenie... to co napisales tutaj to srednia arytmetyczna
    dzielenie = l[0]
    for liczba in l[1:]:
        try:
            dzielenie /= liczba
        except ZeroDivisionError:
            print("Pamietaj cholero, nie dziel przez zero!")
    print('Wynik dzielenia: ', dzielenie)
else:
    print('Niestety nie ogarniasz')
