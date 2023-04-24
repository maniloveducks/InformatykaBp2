NrOfWindows = int(input('podaj liczbe okien: '))
NrOfSpacesHor = int(input('podaj liczbe okien w poziomie: '))
NrOfSpacesVer = int(input('podaj liczbe spacji w pionie: '))

ladder = '#'
star = '*'
space = ' '

lenght = (NrOfWindows-1) * 3 + (NrOfSpacesHor * NrOfWindows) + 4


print (lenght)

print(lenght*ladder)

for i in range(1,NrOfWindows+1):
    print(ladder, star*(NrOfSpacesHor+2), sep='', end='')
print(ladder)

for y in (1, NrOfSpacesVer+1):
    for z in range(1,NrOfWindows+1):
        print(ladder+star+NrOfSpacesHor*space+star, end='')
    print(ladder)
   

for i in range(1,NrOfWindows+1):
    print(ladder, star*(NrOfSpacesHor+2), sep='', end='')
print(ladder)
print(lenght*ladder)












