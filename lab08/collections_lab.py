# Лабораторная работа 8. Вариант 1

#Задание 1
def word_counts(text):
    counts = {}
    for word in text.lower().split():
        word = word.strip('.,!?;:')
        if word:
            counts[word] = counts.get(word, 0) + 1
    return counts

def print_word_counts(counts):
    for word in sorted(counts):
        print(word + ':', counts[word])

#Задание 2
def common_topics(first, second):
    return sorted(set(first) & set(second))

def all_topics(first, second):
    return sorted(set(first) | set(second))

#Вариант 1(задание 3 делается в "Запуск функций" в файле collections_lab.py)
 '''
Пример значения из задания:
records = [
    {"title": "A", "category": "основное", "amount": 4},
    {"title": "B", "category": "дополнительное", "amount": 2},
    {"title": "C", "category": "основное", "amount": 3},
]
'''
def totals_by_category(records):
    totals = {}
    for record in records:
        category = record['category']
        totals[category] = totals.get(category, 0) + record['amount']
    return totals

def titles_in_category(records, category):
    titles = []
    for record in records:
        if record['category'] == category:
            titles.append(record['title'])
    return titles

#Доп задание
def sorted_category_totals(records):
    totals = totals_by_category(records)
    pairs = list(totals.items())
    return sorted(pairs, key=lambda pair: (-pair[1], pair[0]))

#Запуск функций
def main():
    print('Задание 1. Частоты слов')
    text = input('Введите текст: ')
    counts = word_counts(text)
    if counts:
        print_word_counts(counts)
    else:
        print('{}')

    print('\nЗадание 2. Учебные интересы')
    first = ['python', 'sql', 'python']
    second = ['sql', 'git']
    print('Общие темы:', common_topics(first, second))
    print('Все темы:', all_topics(first, second))

    print('\nЗадание 3. Запись и пара')
    lesson = {'title': 'Python', 'hours': 4}
    lesson['hours'] = 6
    lesson['completed'] = False
    pair = (lesson['title'], lesson['hours'])
    title, hours = pair
    print('Словарь:', lesson)
    print('Кортеж:', pair)
    print('Название:', title)
    print('Часы:', hours)

    print('\nВариант 1. Учебные занятия')
    records = [
        {'title': 'Математика', 'category': 'точные науки', 'amount': 4},
        {'title': 'Программирование', 'category': 'точные науки', 'amount': 6},
        {'title': 'История', 'category': 'гуманитарные', 'amount': 2},
        {'title': 'Английский язык', 'category': 'языки', 'amount': 3},
        {'title': 'Русский язык', 'category': 'языки', 'amount': 2},
        {'title': 'Информационная безопасность', 'category': 'точные науки', 'amount': 5}
    ]

    totals = totals_by_category(records)
    print('Всего часов по категориям:')
    for category in sorted(totals):
        print(category + ':', totals[category])

    category = input('Введите категорию для поиска: ')
    print('Занятия:', titles_in_category(records, category))

    print('Категории по убыванию часов:', sorted_category_totals(records))

if __name__ == '__main__':
    main()
