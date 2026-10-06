rejected = 0
number = int(input('Введите положительное число: '))

while number <= 0:
    rejected += 1
    number = int(input('Введите положительное число: '))

print('Квадрат:', number*number)
print('Отклонено:', rejected)
