N = int(input("liczba calkowita dodatnia: "))
sumk= 0 
while N<0 :
    N = int(input("liczba calkowita dodatnia: "))
    
for i in range(1,N+1):
    if N % i == 0:
        sumk += 1
        
if sumk==2 : 
    print(N, 'jest liczba pierwsza')
else:
    print(N, 'nie jest liczba pierwsza')
        
