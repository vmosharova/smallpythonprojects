import random as r
a = int(input()) #множество всех возможных исходов
b = [int(i) for i in input().split()] #благоприятные исходы
c = len(b)/a
theorchislo = round(c*10**6) #количество благоприятных исходов при 10**6 экспериментов
counterrealchislo = 0
for i in range(10**6):
   realchislo = r.randint(0, a - 1)
   if realchislo in b:
       counterrealchislo +=1
print(theorchislo)
print(counterrealchislo)

