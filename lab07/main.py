from functions import*

#1
def main():
    number=int(input('Введите целое число: '))
    print('Сумма цифр:', sum_digits(number))
#2
    numbers_text=input('Введите целые числа через пробел: ')
    numbers=[]
    for item in numbers_text.split():
        numbers.append(int(item))
    result = average(numbers)
    if result is None:
        print('Нет данных')
    else:
        print('Среднее:', result)
#3
    text = input('Введите текст: ')
    print('Нормализованный текст:', normalize_text(text))
#4
    threshold = int(input('Введите неотрицательный порог: '))
    if threshold < 0:
        print('Порог не может быть отрицательным')
        return
    print('Числа больше порога:', select_numbers(numbers, threshold))
if __name__=='__main__':
    main()
