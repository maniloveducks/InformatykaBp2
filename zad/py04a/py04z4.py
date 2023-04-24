import math as M
start = float(input("Podaj początek przedziału: "))
num = int(input("Podaj liczbę podprzedziałów: "))
leng = float(input("Podaj dlugosc podprzedziałów: "))
degree = start 

for i in range(0, num):
    print("sin(", degree, ") =", M.sin(degree))
    degree += leng
