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

print(
    'Условия:\n   СЛОТЫ БЛЯДЬ \n   Кукуруза - К, \n   Печень - П, \n   Zov - Z, \n   Овечка - О, \n   Гитлер - Г, \n   Стася стерва - Н, \n   kick здорового человека - V')

#К G Z О Г Н V
def board(gambling):
    if gambling == True:
        while (x < 5):
            for i in range(len(matrix)):
                matrix[i] = random.randint(1, 7)
                if matrix[i] == 1:
                    krutka = 'К'
                if matrix[i] == 2:
                    krutka = 'G'
                if matrix[i] == 3:
                    krutka = 'Z'
                if matrix[i] == 4:
                    krutka = 'О'
                if matrix[i] == 5:
                    krutka = 'Г'
                if matrix[i] == 6:
                    krutka = 'Н'
                if matrix[i] == 7:
                    krutka = 'V'
            print(matrix)
        else:
            return False
