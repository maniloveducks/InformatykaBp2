liczb = int(input('liczba calk dodatnia: '))
print('dzielniki: ')
liczba = 0
if liczb< 0 :
    print('niet')
else:
    for i in range(1, liczb+1):
        if liczb%i == 0:
            liczba += 1
print(liczba)
       
