import random
startCash = 2_000_000
stavkaStart = 25_000
slot = ''
x = True
matrix = [['', '', '', '', ''],
          ['', '', '', '', ''],
          ['', '', '', '', ''],
          ['', '', '', '', ''],
          ['', '', '', '', '']]

print(' СЛОТЫ БЛЯДЬ \n Кукуруза - К, \n Печень - П, \n Zov - Z, \n Овечка - О, \n Гитлер - Г, \n Стася стерва - Н, \n kick здорового человека - V')


randomInt = random.randint(1, 7)
if randomInt == 1:
    krutka = 'К'
if randomInt == 2:
    krutka = 'G'
if randomInt == 3:
    krutka = 'Z'
if randomInt == 4:
    krutka = 'О'
if randomInt == 5:
    krutka = 'Г'
if randomInt == 6:
    krutka = 'Н'
if randomInt == 7:
    krutka = 'V'


for i in range (len(matrix)):
    matrix[i] = krutka

print(matrix)