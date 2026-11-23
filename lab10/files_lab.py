from pathlib import Path

def read_matrix(path):
    with open(path, 'r', encoding='utf-8') as file:
        lines = file.read().splitlines()
        
    if not lines:
        raise ValueError('Строка 1: файл пустой')
    
    header = lines[0].split()
    if len(header) != 2:
        raise ValueError('Строка 1: ожидалось два целых числа')
    try:
        rows, columns = map(int, header)
    except ValueError:
        raise ValueError('Строка 1: размеры должны быть целыми числами') from None
    if rows <= 0 or columns <= 0:
        raise ValueError('Строка 1: размеры должны быть больше нуля')
    matrix = []
    for index in range(rows):
        line_number = index + 2
        if index + 1 >= len(lines):
            raise ValueError(f'Строка {line_number}: не хватает строки таблицы')
        parts = lines[index + 1].split()
        if len(parts) != columns:
            raise ValueError(f'Строка {line_number}: ожидалось {columns} чисел')
        try:
            row = [int(number) for number in parts]
        except ValueError:
            raise ValueError(f'Строка {line_number}: найдено нецелое число') from None
        matrix.append(row)

    if len(lines) > rows + 1:
        raise ValueError(f'Строка {rows + 2}: лишняя строка в файле')
    return matrix


def selected_sum(matrix):
    # Индивидуальный вариант 1: сумма положительных элементов.
    return sum(number for row in matrix for number in row if number > 0)
