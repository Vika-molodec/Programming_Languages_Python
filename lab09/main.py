from table import*

# Ввод таблицы
rows = int(input('Количество строк: '))
while rows < 1:
    rows = int(input('Введите положительное количество строк: '))

columns = int(input('Количество столбцов: '))
while columns < 1:
    columns = int(input('Введите положительное количество столбцов: '))

matrix = []
for index in range(rows):
    row = [int(number) for number in input(f'Строка {index + 1}: ').split()]
    while len(row) != columns:
        print(f'Нужно ровно {columns} чисел')
        row = [int(number) for number in input('Повторите строку: ').split()]
    matrix.append(row)

# Задания 1 и 2. Суммы строк и столбцов
print('\nСуммы строк:', row_sums(matrix))
print('Суммы столбцов:', column_sums(matrix))

# Задание 3. Диагональный узор
size = int(input('\nРазмер диагонального узора: '))
while size < 1:
    size = int(input('Введите положительный размер: '))

print('Диагональный узор:')
for row in diagonal_pattern(size):
    print(*row)

# Индивидуальный вариант 1. Отрицательные заменить нулями
print('\nИсходная таблица:')
for row in matrix:
    print(*row)

print('Преобразованная таблица:')
new_matrix = transform(matrix)
for row in new_matrix:
    print(*row)
