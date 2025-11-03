# -> Zadanie 13

import random
#dołączenie modułu
n = 5

liczba = random.randint(0, 100)
print('Wylosowana liczba:', liczba)

min_liczba = liczba
max_liczba = liczba
suma = liczba

for i in range(n-1):
    liczba = random.randint(0, 100)
    print('Wylosowano:', liczba)
    if liczba < min_liczba:
        min_liczba = liczba
    if liczba > max_liczba:
        max_liczba = liczba
    suma = suma + liczba
    
srednia = suma / n

print('Najmniejsza liczba:', min_liczba)
print('Największa liczba:', max_liczba)
print('Średnia:',srednia) 