wys1 = int(input("wys1: "))
wys2 = int(input("wys2: "))
wys3 = wys1 + wys2
star = '*'
space = " "
y = 1
print(space*(wys3-1) + star)

for i in range(1, wys1):
    print(space*(wys3-(i+1)) + star + y*space + star)
    y+=2
    
print((wys2-1)*space + (y+2)*star)

for i in range(1, wys2):
    print((wys2-1)*space + star + y*space + star)
