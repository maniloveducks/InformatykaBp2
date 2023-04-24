N = int(input("liczba calkowita dodatnia: "))
sumk=0
while N<0 :
    N = int(input("liczba calkowita dodatnia: "))
print('Suma licznikow: ')
for i in range(1,N+1):
    if N % i == 0:
        sumk+= i
print(sumk)




