n = int(input('Введите n: '))
count = 0
total = 0
for i in range(n):
    number = int(input('Введите число: '))
    if number % 2 == 0:
        count += 1
        total += number
print('Количество:', count)
print('Сумма:', total)
