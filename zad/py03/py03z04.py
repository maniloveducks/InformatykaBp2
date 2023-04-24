dochod = float(input('dawaj dochod: '))
if dochod < 85528:
    print('jestes w nizszej kategorii podatkowej')
    podatek = (dochod * 0.18) - 556.02
    if podatek >=0:
        print('podatek wynosi :', podatek, 'PLN')
        print('zostajesz z:', dochod - podatek)
    elif podatek<0:
        print('podatek wynosi 0 PLN')
        print('zostajesz z:', dochod)
elif dochod >= 85528:
    podatek = 14839.02 + 0.32*(dochod - 85528)
    print('jestes w wyzszej kategorii podatkowej')
    print('podatek wynosi :', podatek, 'PLN')
    print('zostajesz z:', dochod - podatek)

