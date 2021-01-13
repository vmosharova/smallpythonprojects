commands = ['+', '-', '<', '>', '[', ']', '.', ',']
programm = list(input())
for symbol in programm:
    if symbol not in commands:
        programm.remove(symbol)
dict = {}
temp = []
for i, symb in enumerate(programm):
    if symb == '[':
        temp.append(i)
    elif symb == ']':
        dict[temp[-1]] = i
        dict[i] = temp[-1]
        temp.pop()
index_command = 0
a = []
for zero in range(30000):
    a.append(0)
index = 15000
while index_command < len(programm):
    Flag = True
    if programm[index_command] == '+':
        a[index] += 1
    elif programm[index_command] == '-':
        a[index] -= 1
    elif programm[index_command] == '>':
        index += 1
    elif programm[index_command] == '<':
        index -= 1
    elif programm[index_command] == ',':
        a[index] -= ord(input())
    elif programm[index_command] == '.':
        print(chr(a[index]), end='')
    elif programm[index_command] == '[':
        Flag = False
        if a[index] == 0:
            index_command = dict[index_command] + 1
        else:
            index_command += 1
    elif programm[index_command] == ']':
        Flag = False
        if a[index] != 0:
            index_command = dict[index_command]
        else:
            index_command += 1
    if Flag:
        index_command += 1