# TheProjectOfGame
MAX_LINES = 3



# Ставка
def deposit():
    while True:
        amount = input('Ваша ставка? "Р" ')
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print('Ставка должна быть больше ноля')
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

def main():
    balance = deposit()
    lines = get_number_of_lines()
    print(balance, lines)

main()