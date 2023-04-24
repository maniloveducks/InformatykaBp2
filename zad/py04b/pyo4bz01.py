wys = int(input("wysokosc: "))
space = ' '
star = '*'
y = wys-3

print(star, space*(wys*y), star, sep='')

for i in range (1, wys-1):
    print(star,space*i,star,  space*(y+i), star,space*i,star, sep='')
  
    

    


print(star, i*space, star, i*space, star, sep='')
print( y, abs(y))
    

