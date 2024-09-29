import math

# Zadanie 1
# Napisz program ktory bedzie dzialal jako kalkulator.
# Podstawowa funkcjonalnosc to ponizsze operacje:
# - dodawanie
# - odejmowanie
# - mnozenie
# - dzielenie
#
# Program powinien przyjmowac minimum 2 argumenty:
# - operacja
# - liczby (w jakiejkolwiek postaci, np jedna po drugiej albo jako lista oddzielona znakiem ",")
#
# Mozesz dodac wiecej operacji, im wiecej tym lepiej.


# funkcje pomocnicze kalkulatora
def pytaj_o_opreracje(lista_operacji: list[str]) -> str:
    correct = False
    while not correct:
        user_input = input(
            f"Podaj jakiej operacji chcec uzyc - {lista_operacji}: ")

        if user_input not in lista_operacji:
            print("Podaj poprawna operacje!")
        else:
            correct = True

    return user_input


def pobierz_x_liczb(x: int) -> list[float]:
    liczby: list[float] = []

    for i in range(x):
        user_input: float = 0
        correct = False
        while not correct:
            user_input_str = input(f"Podaj {i + 1} liczbe: ")

            try:
                user_input = float(user_input_str)
                correct = True
            except ValueError:
                print("Podaj wartosc zmiennoprzecinkowa!")

        liczby.append(user_input)

    return liczby


def iteracja_kalkulatora():
    operacje = ['+', '-', '*', '/', '^', 'sin', 'cos', 'delta']

    wybrana_operacja = pytaj_o_opreracje(operacje)

    match wybrana_operacja:
        case '+':
            [a, b] = pobierz_x_liczb(2)

            print(a + b)

        case '-':
            [a, b] = pobierz_x_liczb(2)

            print(a - b)

        case '*':
            [a, b] = pobierz_x_liczb(2)

            print(a * b)

        case '/':
            [a, b] = pobierz_x_liczb(2)

            if b == 0:
                print("Proba dzielenia przez 0.")
            else:
                print(a / b)

        case '^':
            [a, b] = pobierz_x_liczb(2)

            if a == 0 and b == 0:
                print("Proba podniesienia 0 do 0 potegi - wyrazenie nieoznaczone.")
            else:
                print(a ** b)

        case 'sin':
            [a] = pobierz_x_liczb(1)

            print(math.sin(a))

        case 'cos':
            [a] = pobierz_x_liczb(1)

            print(math.cos(a))

        case 'delta':
            [a, b, c] = pobierz_x_liczb(3)

            delta = b ** 2 - 4 * a * c

            print(delta)


def kalkulator():
    kontynuuj = True
    while kontynuuj:
        iteracja_kalkulatora()

        user_input = ''
        while True:
            user_input = input(
                "Czy chec wykonac inna operacje czy zakonczyc? Wpisz 'next' (by kontynuowac) lub 'stop' (aby zakonczyc): ")

            if user_input in ['next', 'stop']:
                break
            else:
                continue

        if user_input == 'stop':
            kontynuuj = False


kalkulator()


# Zadanie 2
# Poszukaj: algorytmy sortujące listy
#
# Napisz zestaw funkcji ktora sortuje liste liczb.
# Testowac bedziemy na listach o dlugosci do 100_000 elementow.
# Elementy beda zawsze liczbami calkowitymi.
#
# Nie korzystaj z zadnych gotowych funkcji sortujacych z Pythona.
# Wolno ci korzystac z funkcji pomocniczych, ktore napiszesz
# sam oraz z podstawowych operatorow oraz operacji (while, for, if itp).


def posortuj(lista: list[int]) -> list[int]:
    pass


print(posortuj([1, 4, 12, 3]))  # -> [1, 3, 4, 12]
print(posortuj([1, 4, 12, 3]))  # -> [1, 3, 4, 12]
print(posortuj([1, 4, 12, 3]))  # -> [1, 3, 4, 12]
print(posortuj([1, 4, 12, 3]))  # -> [1, 3, 4, 12]

# Zadanie 3
# Napisz funkcje ktora zwroci mi n-ta liczbe z ciagu Fibonacciego.
# Zakladamy ze 1-wszy element ciagu to 1 a 2-gi to 1.
# Wtedy:
# 3-ci to 2,
# 4-ty to 3,
# 5-ty to 5,
# itd.
#
# Mozesz napisac rozwiazanie rekurencyjnie lub iteracyjnie.
# Jezeli nie wiesz co znacza te pojecia, mozesz sie z nimi zaznajomic lub je zignorowac.
# Znajomosc tych pojec nie jest potrzebna do napisanie rozwiazania.
#
# Jezeli wpisze w takim razie ze chce 5-ta liczbe z ciagu Fibonacciego, to funkcja powinna zwrocic 5.
# Jezeli wpisze 10-ta liczbe, to funkcja powinna zwrocic 55, itd.
