b = [['*' for i in range(3)] for k in range(3)]
Flag = False
win = 0
n = 0
while Flag == False and n < 9:
    coordinates_1 = input().split() #игроки вводят координаты крестиков
    x = int(coordinates_1[0]) - 1
    y = int(coordinates_1[1]) - 1

    if n % 2 == 0:
        b[x][y] = 'X'
    else:
        b[x][y] = '0'

    for i in b:
        for k in i:
            print(k, end=' ')
        print()
    z = 0
    for z in range(3):  # проверяем горизонтальные
        if b[z][0] == b[z][1] == b[z][2] != '*':
            win = b[z][0]
            Flag = True
        elif b[0][z] == b[1][z] == b[2][z] != '*': # проверяем вертикальные
            win = b[0][z]
            Flag = True
            z += 1
    if b[0][0] == b[1][1] == b[2][2] != '*': #диагональ
        win = b[0][0]
        Flag = True
    elif b[2][0] == b[1][1] == b[0][2] != '*':
        win = b[2][0]
        Flag = True
    n += 1

if win == 'X':
    print('X wins')
elif win == '0':
    print('0 wins')
else:
    print('It\'s A Draw (nobody wins)')