liczb = int(input('liczba calk dodatnia: '))
print('dzielniki: ')
if liczb< 0 :
    print('niet')
else:
    for i in range(1, liczb+1):
        if liczb%i == 0:
            print(i)

       
