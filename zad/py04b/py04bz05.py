N = int(input('liczba n: '))
suma = 0
if N == 0:
    print('niet')
else:
    for i in range(1, N+1) :
        liczb = int(input('liczba: '))
        suma = suma + liczb
    
    print(suma)
