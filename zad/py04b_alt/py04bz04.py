HeightSH = int(input('podaj wysokosc z linia: '))
NrOfShapes = int(input('podaj liczbe ksztaltow: '))
star = '*'
space = ' '
y1= 1
f1= 2

for i in range(1,HeightSH):
    for z in range(1, NrOfShapes+1):
        print(space*(HeightSH-i) + star*y1 + space*(HeightSH-f1),end='')  
    y1+=2
    f1+=1
    print('')

B = y1-1
print( NrOfShapes*(star*B) + star )

y1 -= 2
G = 0
for i in range(1,HeightSH):
    for z in range(1,NrOfShapes+1):
        print(space*(i) + star*y1 + space*G ,end='' )
    print('')
    y1-=2
    G += 1
   


"""
   *     *     *   
  ***   ***   ***  
 ***** ***** ***** 
*******************
 ***** ***** ***** 
  ***   ***   ***  
   *     *     *   
"""
