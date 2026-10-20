#Вариант 1: слова, начинающиеся с буквы 'а'
text = input('Введите текст: ')
count = 0
for word in text.split():
    word = word.strip('.,!?;:').lower()
    if not word:
        continue
    if word.startswith('а'):
        print(word)
        count += 1
if count == 0:
    print('Нет совпадений')
print(f'Количество: {count}')
