text = input('Введите текст: ')
cleaned = text.lower().replace(' ', '')
if not cleaned:
    print('Нет текста')
elif cleaned == cleaned[::-1]:
    print('Палиндром')
else:
    print('Не палиндром')
