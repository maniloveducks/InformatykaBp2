wys = int(input("podaj wysokosc: "))
star = '*'
y = 1
x = wys
space = ' '
for i in range(1, (2*wys)+1 ):
    if i in range(1, wys+1):
        print(space*(wys-i) + star*y)
        y +=2
    else:
        print(space*(i-wys) + star*(x+1))
        x-=2
        
             
    
    
             
    
   
    
    
