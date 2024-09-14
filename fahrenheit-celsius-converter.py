# (°F) = ((°C) * 9/5) + 32
# (°C) = ((°F) - 32) * 5/9
# (°K) = (°C) + 273.15
# (°C) = (°K) - 273.15

def f_to_c(fahrenheit):
    celciusz = (fahrenheit-32) * 5/9
    return celciusz


def c_to_f(celciusz):
    fahrenheit = (celciusz / (5/9)) + 32
    return fahrenheit


def k_to_c(kelvin):
    celciusz = kelvin - 273.15
    return celciusz


def c_to_k(celciusz):
    kelvin = celciusz + 273.15
    return kelvin


dostepne_wybory = ['c', 'f', 'k']

od = ''
do = ''
while od not in dostepne_wybory or do not in dostepne_wybory:
    od = input(f"Co chesz obliczyc?\n{'\n'.join(list(map(lambda x: '- ' + x, dostepne_wybory)))}\n")
    do = input(f"Na co chcesz przeliczyc?\n{'\n'.join(list(map(lambda x: '- ' + x, dostepne_wybory)))}\n")

    if od in dostepne_wybory and do in dostepne_wybory:
        break

    print(f'Zły wybór, wpisz {" lub ".join(dostepne_wybory)}')

mapa_obliczen = {
    'c': {
        'f': lambda x: c_to_f(x),
        'k': lambda x: c_to_k(x),
        'c': lambda x: x,
    },
    'f': {
        'f': lambda x: x,
        'c': lambda x: f_to_c(x),
        'k': lambda x: c_to_k(f_to_c(x)),
    },
    'k': {
        'f': lambda x: c_to_f(k_to_c(x)),
        'c': lambda x: k_to_c(x),
        'k': lambda x: x,
    }
}

wartosc = float(input(f'Podaj wartosc °{od}: '))

resultat = mapa_obliczen[od][do](wartosc)

print(f"{wartosc} °{od} to {resultat} °{do}")


# c = (f-32) * 5/9        | /(5/9)
# c / (5/9) = f-32    | +32
# c / (5/9) + 32 = f
