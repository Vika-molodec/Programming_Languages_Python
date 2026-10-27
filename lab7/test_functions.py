from functions import average, is_palindrome, normalize_text, select_numbers, sum_digits

# Основные функции(их три)
assert sum_digits(0) == 0
assert sum_digits(507) == 12
assert sum_digits(-507) == 12
assert sum_digits(1000) == 1

assert average([]) is None
assert average([2, 4, 6]) == 4
assert abs(average([1, 2]) - 1.5) < 1e-9

numbers = [1, 2, 3]
original = numbers.copy()
assert average(numbers) == 2
assert numbers == original

assert normalize_text('  ПРИВЕТ   Мир  ') == 'привет мир'
assert normalize_text('   ') == ''
assert normalize_text('  Один\tдва\nтри  ') == 'один два три'
print('Базовые проверки пройдены')

# Вариант 1 - числа строго больше порога
assert select_numbers([-5, 0, 2, 5], 2) == [5]
assert select_numbers([], 2) == []
assert select_numbers([1, 2, 3], 2) == [3]
assert select_numbers([0, 1, 2], 5) == [] 
assert select_numbers([0, 1, 2], 1) == [2]
assert select_numbers([3, 3, 2, 4], 2) == [3, 3, 4]

numbers = [-5, 0, 2, 5, 5]
original = numbers.copy()
assert select_numbers(numbers, 2) == [5, 5]
assert numbers == original
print('Проверки варианта 1 пройдены')

# Дополнительное задание - палиндром (правила работы №5)
assert is_palindrome('А роза упала на лапу Азора') is True
assert is_palindrome('а    ') is True
assert is_palindrome('   ') is False
assert is_palindrome('') is False
assert is_palindrome('Python') is False
assert is_palindrome('А!') is False
print('Дополнительные проверки пройдены')
