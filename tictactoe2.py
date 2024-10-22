import random

def draw_board(slots):
    board = (f'|{slots[1]}|{slots[2]}|{slots[3]}|\n'
             f'|{slots[4]}|{slots[5]}|{slots[6]}|\n'
             f'|{slots[7]}|{slots[8]}|{slots[9]}|')
    print(board)

def count_turns(turn):
    return "O" if turn % 2 == 0 else "X"

def check_win(slots):
    # Проверка строк, колонок и диагоналей
    return ((slots[1] == slots[2] == slots[3]) or
            (slots[4] == slots[5] == slots[6]) or
            (slots[7] == slots[8] == slots[9]) or
            (slots[1] == slots[4] == slots[7]) or
            (slots[2] == slots[5] == slots[8]) or
            (slots[3] == slots[6] == slots[9]) or
            (slots[1] == slots[5] == slots[9]) or
            (slots[3] == slots[5] == slots[7]))

def ai_move(slots, turn):
    """Логика компьютера для выбора хода."""
    player = count_turns(turn)  # Текущий игрок компьютер ('X' или 'O')
    opponent = 'O' if player == 'X' else 'X'
    
    # Вспомогательная функция для поиска свободных ячеек
    def available_slots(slots):
        return [key for key, value in slots.items() if value not in {'X', 'O'}]

    # Проверка, может ли компьютер выиграть
    for move in available_slots(slots):
        slots_copy = slots.copy()
        slots_copy[move] = player
        if check_win(slots_copy):
            return move  # Сделать победный ход

    # Проверка, нужно ли компьютеру блокировать выигрышный ход соперника
    for move in available_slots(slots):
        slots_copy = slots.copy()
        slots_copy[move] = opponent
        if check_win(slots_copy):
            return move  # Заблокировать соперника

    # Занять центральную ячейку, если она свободна
    if slots[5] == '5':
        return 5

    # Занять один из углов, если они свободны
    for corner in [1, 3, 7, 9]:
        if slots[corner] not in {'X', 'O'}:
            return corner

    # Занять любую оставшуюся свободную ячейку
    return random.choice(available_slots(slots))

# Инициализация игрового поля
slots = {i: str(i) for i in range(1, 10)}

ai = False
playing = False
complete = False
turn = 0
prev_turn = -1
player_first = True  # Переменная для хранения выбора игрока: идет ли он первым

# Выбор режима игры
pre = input("Хотите играть с другом или компьютером? Введите F для друга или A для компьютера: ")
if pre.lower() == 'a':
    ai = True
    # Выбор, кто ходит первым: игрок или компьютер
    order = input("Хотите идти первым? Введите Y для да или N для нет: ")
    if order.lower() == 'n':
        player_first = False
elif pre.lower() == 'f':
    playing = True
else:
    print("Вы ввели неправильную букву.")

# Цикл игры с компьютером
while ai and not complete:
    draw_board(slots)
    
    # Проверка, ход игрока или компьютера
    if (turn % 2 == 0 and not player_first) or (turn % 2 == 1 and player_first):
        # Ход компьютера
        choice = ai_move(slots, turn)
        print(f"Компьютер выбрал {choice}")
    else:
        # Ход игрока
        choice = input("Введите номер ячейки или q для выхода: ")

    if choice == 'q':
        ai = False
    elif str(choice).isdigit() and int(choice) in slots:
        choice = int(choice)
        if slots[choice] not in {"X", "O"}:  # Убедиться, что ячейка свободна
            turn += 1
            slots[choice] = count_turns(turn)  # Поставить X или O только на свободную ячейку
        else:
            print("Место уже занято, выберите другое.")
    else:
        print("Неверный выбор, попробуйте еще раз.")
    
    # Проверка на победу
    if check_win(slots):
        ai, complete = False, True
    if turn > 8:  # Если все ячейки заняты
        ai = False

# Цикл игры для двух игроков
while playing and not complete:
    draw_board(slots)
    print(f"Ход игрока {str((turn % 2) + 1)}")
    
    choice = input("Введите номер ячейки или q для выхода: ")
    if choice == 'q':
        playing = False
    elif choice.isdigit() and int(choice) in slots:
        choice = int(choice)
        if slots[choice] not in {"X", "O"}:  # Проверить, свободна ли ячейка
            turn += 1
            slots[choice] = count_turns(turn)
        else:
            print('Место уже занято, выберите другое.')
    else:
        print("Неверный выбор, попробуйте еще раз.")
    
    # Проверка на победу
    if check_win(slots):
        playing, complete = False, True
    if turn > 8:  # Если все ячейки заняты
        playing = False

# Конец игры
if complete:
    if count_turns(turn) == "X":
        print('Игрок 1 победил')
    else:
        print('Игрок 2 победил')
else:
    print('Ничья')

# Отобразить финальное состояние доски
draw_board(slots)
