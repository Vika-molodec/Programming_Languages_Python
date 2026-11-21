# Дополнительный модуль. Рекурсия

# Рекурсивное вычисление факториала
def factorial(number):
    if number == 0:
        return 1
    return number * factorial(number - 1)

# Вычисление факториала с помощью цикла
def factorial_loop(number):
    result = 1
    for value in range(1, number + 1):
        result *= value
    return result

for number in range(21):
    assert factorial(number) == factorial_loop(number)
assert factorial(0) == 1
assert factorial(5) == 120
print('Проверка рекурсивного и циклического факториала прошла успешно')
