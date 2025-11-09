# --> Zadanie_14

print('Menu:')
print('(1) Celsjusz -> Fahrenheit')
print('(2) Fahrenheit -> Celsjusz')
print('(k) koniec')

while True:
    jednostka = input('Wybierz opcje:' )
    
    if jednostka == '1':
        temperatura = float (input('Podaj wartość:'))
        print((temperatura - 32)* 5/9, 'Fahrenheitów')
    elif jednostka == '2':
        temperatura = float (input('Podaj wartość:'))
        print((temperatura * 9/5) + 32, 'stopni Celsjusza')
    elif jednostka == 'k':
        print('Koniec.')
        break
    
    else:
        print('Niepoprawny wybór, spróbuj ponownie')