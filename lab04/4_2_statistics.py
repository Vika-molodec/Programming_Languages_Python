n = int(input('Введите n: '))
number = int(input('Введите число: '))
total = number
positive_count = 1 if number > 0 else 0
maximum = number
for i in range(n - 1):
    number = int(input('Введите число: '))
    total += number

    if number > 0:
        positive_count += 1

    if number > maximum:
        maximum = number
print('Сумма:', total)
print('Положительных:', positive_count)
print('Максимум:', maximum)
