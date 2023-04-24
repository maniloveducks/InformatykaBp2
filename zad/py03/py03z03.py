x = int(input("poodaj liczbe calkowita: "))
999
if x > 0 and x<9999:        
    tys = int(x/1000)
    setk = int((x-tys*1000)/100)
    dzies = int((x-(tys*1000 + setk * 100))/10)
    jedn = int(x-(tys*1000 + setk*100 + dzies*10))
    print('liczba to:', x)
    print('liczba tysiecy:', tys )
    print('liczba setek:', setk  )
    print('liczba dziesiatek:', dzies)
    print('liczba jednosci:', jedn)
else:
    print('błędzik')

  
