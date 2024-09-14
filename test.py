# Stworz liste numerow od 1 do 10 co 0.5, nastepnie wypisz tylko te ktore sa parzyste
# uzyj for oraz range

start = 1
end = 10
step = 0.5

number_count = int((end - start) / step) + 1

lista = []
for i in range(number_count):
    lista.append(start + i * step)

for numer in lista:
    if numer % 2 == 0:
        print(numer)


