m = int(input("liczba calkowita1: "))
sumk = 1

for n in range(1, m+1):
    sumk *= (4*(n**2))/(4*(n**2)-1)
print(2*sumk)

