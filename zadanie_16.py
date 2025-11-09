# -> Zadanie 16
import random

odpowiedź = random.randint(1, 100)

próby = 0

print('Zagraj w grę!')
print('Zganij liczbę!')
print('{liczba od 1 do 100}')

while True:
    liczba = int(input('Podaj liczbę:' ))
    próby = próby + 1
    
    if liczba > odpowiedź :
        print('Ta liczba jest za duża, próbuj dalej!')
    if liczba < odpowiedź :
        print('Ta liczba jest za mała, próbuj dalej!')
    if liczba == odpowiedź :
        print(f'Gratulacje!! Odgadłeś liczbę {odpowiedź} w {próby} próbach. ')
        break 