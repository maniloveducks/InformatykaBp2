x = float(input("Podaj pierwszą liczbę: "))
y = float(input("Podaj drugą liczbę: "))
dzial = input("Podaj działanie (+, -, *, /): ")
if dzial != '+' and '-' and '*' and '/' :
    print("nieznane działanie")
else:
    

    if dzial == '+'  :
        c = x+y
        print(x, '+',  y, '=', c)

    elif dzial == '-' :
        c = x-y
        print(x, '-',  y, '=', c)

    elif dzial == '*' :
        c = x*y
        print(x, '*',  y, '=', c)

    elif dzial == '/' and y != 0 :
        c = x/y
        print(x, '/', y, '=', c)
    else: 
        print("blad")
   
   
nie wiem
        
    
        
