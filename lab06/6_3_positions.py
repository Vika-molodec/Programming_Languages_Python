numbers = []
for part in input('Введите целые числа через пробел: ').split():
    numbers.append(int(part))
if not numbers:
    print('Нет данных')
else:
    maximum = max(numbers)
    positions = []
    for index, number in enumerate(numbers):
        if number == maximum:
            positions.append(index)
    print('Индексы максимума:', positions)
