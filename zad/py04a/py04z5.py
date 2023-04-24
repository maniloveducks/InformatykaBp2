wys = int(input("wys: "))
szer = int(input("szer: "))
star = '*'
dot = '.'
for i in range(0, wys):
   if i in range(1, wys-1):
       print(star + (dot*(szer-2)) + star)
   else:
       print(star*szer)
   
