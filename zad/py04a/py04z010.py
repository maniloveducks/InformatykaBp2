wys = int(input('wysokosc: '))
star = '*'
space = ' '
for i in range(1, wys+1):
    print(star + (wys-i)*space + star)
print(star)
for i in range(0, wys):
    print(star + (i*space) + star)
    
