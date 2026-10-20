numbers = []
for part in input('Введите целые числа через пробел: ').split():
    numbers.append(int(part))

if not numbers:
    print('Нет данных')
else:
    print('Количество:', len(numbers))
    print('Сумма:', sum(numbers))
    print('Минимум:', min(numbers))
    print('Максимум:', max(numbers))
    print(f'Среднее: {sum(numbers) / len(numbers):.2f}')
