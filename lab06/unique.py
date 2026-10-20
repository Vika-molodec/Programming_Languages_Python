#Доп задание(удалите повторы, сохранив порядок первого появления, без использования set.)
numbers = []
for part in input('Введите целые числа через пробел: ').split():
    numbers.append(int(part))
unique_numbers = []
for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)
print('Без повторов:', unique_numbers)
