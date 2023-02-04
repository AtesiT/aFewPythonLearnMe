# TheProjectOfGame
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1


# Ставка
def deposit():
    while True:
        amount = input('Сколько вносите в игру? $')
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print('Внос должен быть больше ноля')
        else:
            print('Введите число')
    return amount


# Кол-во строк
def get_number_of_lines():
    while True:
        lines = input('Кол-во строк для ставки (1-' + str(MAX_LINES) + ')? ')
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print('Количество строк должны быть допустимым')
        else:
            print('Введите число')
    return lines

def get_bet():
    while True:
        amount = input('Какую ставку ставить на каждую линию? $')
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f'Сумма должна быть от {MIN_BET} - {MAX_BET} ')
        else:
            print('Введите число')
    return amount


def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f'У тебя недостаточно денег для ставки, ваш баланс ${balance}')
        else:
            break

    print(f'Вы поставили ${bet} на {lines} линий. Общая ставка: ${total_bet}')



    print(balance, lines)
main()