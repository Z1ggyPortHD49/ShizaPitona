import random
import time
import sys

startCash = 2_000_000
delta = 0
stavkaStart = 25_000
slot = ''
x = True
matrix = [['', '', '', '', ''],
          ['', '', '', '', ''],
          ['', '', '', '', ''],
          ['', '', '', '', ''],
          ['', '', '', '', '']]

symbols = {
    1: 'К',  # Кукуруза UA \U0001F1FA\U0001F1E6
    2: 'G',  # ГОЙДА RU "\U0001F1F7\U0001F1FA"
    3: 'Z',  # Zov 🤫 \U0001F92B
    4: 'О',  # Овечка 🐏 \U0001F92B
    5: 'Г',  # Гитлер 👮 \U0001F46E
    6: 'Н',  # Стася стерва 😈 \U0001F608
    7: 'V',  # Кик здорового человека 🍾 \U0001F37E
    8: 'S',  # Arian classic ⚡ \u26A1
    9: 'M',  # Monkey 🐒 \U0001F412
    10: 'R',  # РОДИНА \u262D (☭)
    11: 'U'  # Украина \U0001F437
}


# print("\U0001F4B0")  💰
# print("\U0001F3B0")  🎰
def board(gambling):
    if gambling == True:
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                matrix[i][j] = random.randint(1, 7)
        # for row in matrix:
        #    print(' | '.join(row))
        # print('-' * 25)
        # print(matrix)
    else:
        print('Увё казик закрiт, перемоги и грошей не будэ цсуко\U0001F595')
        return False

print('Дабро пожаловать в казино, пес де патрон')
print('С вашего позволения, как к вам обращаться?' + '\n' + '1 - Не позволяю цсуко. 2 - Ввести имя')
nm = int(input())
if nm == 1:
    print('Ладно тепеь вы El Chuvachini')
    name = 'Эль чувачини'
else:
    time.sleep(1.5)
    print('Значит вы не мразь, вау.', '\n', 'фух... ну введите пожалуйста имя ваше')
    name = input()

while (True):
    print('Нажми 1 чтобы начать крутку, нажми 2 чтобы выйти из окна к примеру')
    gmove = int(input())
    if gmove == 2:
        print('Ну и пошёл нахуй\U0001F595, твой кеш составляет \U0001F449', startCash + delta, '\U0001F448')
        sys.exit(0)
    else:
        print('\U0001F3B0 СЛОТЫ ЗАПУЩЕНЫ')
        board(True)
        print(matrix)
