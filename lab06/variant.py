numbers = []
for part in input('Введите целые числа через пробел: ').split():
    numbers.append(int(part))
even_numbers = []
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
sorted_numbers = sorted(even_numbers)
print('Чётные числа:', even_numbers)
print('Количество:', len(even_numbers))
print('Сумма:', sum(even_numbers))
print('Отсортированная копия:', sorted_numbers)
