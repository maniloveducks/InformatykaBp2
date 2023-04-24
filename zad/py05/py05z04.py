a = int(input("liczba calkowita1: "))
b = int(input("liczba calkowita2: "))
x = float(input("liczba rzeczywista1: "))
y = float(input("liczba rzeczywista2: "))
sumk = 0  
for i in range(a,b+1):
    sumk += (x-i)/(y+i)

print (sumk)
