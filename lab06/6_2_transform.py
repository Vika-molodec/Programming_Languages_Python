numbers = []
for part in input('Введите целые числа через пробел: ').split():
    numbers.append(int(part))
transformed = []
for number in numbers:
    if number < 0:
        transformed.append(-number)
    else:
        transformed.append(number)
print('Исходный список:', numbers)
print('Новый список:', transformed)
