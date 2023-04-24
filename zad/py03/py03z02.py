a = float(input("pierwsza krawedz: "))
b = float(input("druga krawedz: "))
c = float(input("trzecia krawedz: "))
if a > 0 and b> 0 and c >0 :
    p = ( (c**2) + (b**2) + (a**2) )**1/2
    print('przekątna to:', p )
else:
    print('błąd')
