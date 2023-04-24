wys = int(input("WYSOKOSC Z KLAWIATURY: "))
star = '*'
dot = '.'
for i in range(1, wys+1):
    y = wys - i
    print(i*star + y*dot)
    
