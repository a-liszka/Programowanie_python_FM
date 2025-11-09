# -> Zadanie 15

słowo = input('Podaj słowo:').lower()

lista = list(słowo)
print(lista)

if lista == lista[::-1]:
    print('Podane słowo jest PALINDROMEM ')
else:
    print('Podane słowo nie jest PALINDROMEM ')