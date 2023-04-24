N = int(input("liczba calkowita dodatnia: "))
while N<0 :
    N = int(input("liczba calkowita dodatnia: "))
print('Liczniki naturalne to: ')
for i in range(1,N+1):
    if N % i == 0:
        print(i)
        