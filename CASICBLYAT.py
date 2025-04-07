import random
import time
import sys

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
    1: '\U0001F33B',  # 🌻 Кукуруза
    2: '\U0001F43B',  # 🐻 ГОЙДА
    3: '\U0001F92B',  # 🤫 Zov
    4: '\U0001F40F',  # 🐏 Овечка
    5: '\U0001F46E',  # 👮 Гитлер
    6: '\U0001F608',  # 😈 Стася стерва
    7: '\U0001F37E',  # 🍾 Кик
    8: '\u26A1',  # ⚡ Arian classic
    9: '\U0001F412',  # 🐒 Monkey
    10: '\u262D',  # ☭ Родина
    11: '\U0001F437'  # 🐷 Украина
}


def board(roaling):
    if roaling:
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                matrix[i][j] = symbols[random.randint(1, 11)]


def scores():
    global delta, nowCash

    winnings = 0
    matches = []

    # Строки
    for i in range(5):
        row = matrix[i]
        if all(cell == row[0] for cell in row):
            winnings += stavkaStart * 3
            matches.append(f"💥 Строка {i + 1}: 5x {row[0]}")

    # Центр-вертикаль
    center_col = [matrix[i][2] for i in range(5)]
    if all(cell == center_col[0] for cell in center_col):
        winnings += stavkaStart * 4
        matches.append(f"💥 Центр-вертикаль: 5x {center_col[0]}")

    # Джекпот — вся матрица одинаковая
    flat = [cell for row in matrix for cell in row]
    if all(cell == flat[0] for cell in flat):
        jackpot_symbol = flat[0]
        jackpot_win = stavkaStart * 10
        winnings += jackpot_win
        matches.append(f"🎰🎰🎰 ДЖЕКПОТ!!! Вся матрица = {jackpot_symbol} — +💰 {jackpot_win:,}")

    # Минус ставка
    nowCash -= stavkaStart

    if winnings > 0:
        delta += winnings
        print(f"\n🎉 ПОБЕДА! +💰 {winnings:,}")
        for m in matches:
            print(m)
    else:
        print(f"\n😢 Проигрыш. -💸 {stavkaStart:,}")

    total_cash = nowCash + delta
    print(f"\n💼 Баланс игрока: {total_cash:,} 💰")
    print("-" * 45)

    # Если денег нет — вылет
    if total_cash < stavkaStart:
        print("❌ У тебя не осталось денег на ставку. Вылет из казино.")
        print(f"🧾 Финальный счёт: {total_cash:,}")
        sys.exit(0)


# 👋 Приветствие
print('Добро пожаловать в казино, ZOV патрон')
print('С вашего позволения, как к вам обращаться?\n1 - Не позволяю цсуко.\n2 - Ввести имя')
nm = int(input())
if nm == 1:
    print('Ладно, теперь вы El Chuvachini')
    name = 'Эль чувачини'
else:
    time.sleep(1.5)
    print('Значит вы не мразь, вау.\nФух... ну введите, пожалуйста, имя ваше:')
    name = input()

print(f"{name}, введите ваш стартовый капитал. P.S. Меньше 25000 — гарантированный проёб:")
startCash = int(input())
nowCash = startCash

# 🔁 Основной цикл
while True:
    print('\nНажми 1 чтобы начать крутку 🎰\nНажми 2 чтобы выйти из окна')
    gmove = int(input())

    if gmove == 2:
        print(f'Ну и пошёл нахуй 🖕, твой кеш составляет 👉 {nowCash + delta:,} 👈')
        sys.exit(0)

    elif gmove == 1:
        if nowCash + delta < stavkaStart:
            print("💀 У тебя не хватает денег даже на ставку. Ты выбыл.")
            print(f"🪦 Финальный баланс: {nowCash + delta:,} 💸")
            sys.exit(0)

        print('\n🎰 СЛОТЫ ЗАПУЩЕНЫ 🎰\n')
        board(True)
        for row in matrix:
            print(' | '.join(row))
        print("-" * 45)
        scores()

    else:
        print("⚠️ Некорректный ввод. Попробуй снова.")
