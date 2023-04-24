n = int(input("liczba calkowita1: "))
m = int(input("liczba calkowita2: "))
theta = float(input("liczba rzeczywista1: "))
sumk = 0

for i in range(n, m+1):
    sumk1 = 1
    for j in range(i,(i**2)+1):
        sumk1 *= theta/(j*i)
    sumk += sumk1
print(sumk)
