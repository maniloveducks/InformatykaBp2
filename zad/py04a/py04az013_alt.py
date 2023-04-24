
N = int(input('liczba calk: '))
print('1')
for i in range(1,N):
    print('1',end='')
    for j in range(2,i+2):
        print(', ', j, end='', sep='')
    print('\n', end='')
    
