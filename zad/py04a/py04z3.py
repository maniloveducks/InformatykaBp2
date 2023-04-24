wys = int(input("WYSOKOSC Z KLAWIATURY: "))
star = '*'
dot = '.'
for i in range(0, wys+1):
    print(i*star + (i+1)*dot)
