wys = int(input("podaj wysokosc: "))
star = '*'
y = 1
space = ' '
for i in range(1, wys+1):
    print(space*(wys-i) + star*y)
    y+=2
    
    
