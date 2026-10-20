text = input('Введите текст: ')
count = text.count(':')
result = text.replace(':', '-')

print(f'Количество замен: {count}')
print(f'Новая строка: {result}')
