def sum_digits(number):
    number = abs(number)
    digit_sum = 0
    while number > 0:
        digit_sum += number%10
        number //= 10
    return digit_sum


def average(numbers):
    if not numbers:
        return None
    return sum(numbers)/len(numbers)


def normalize_text(text):
    return ' '.join(text.lower().split())


def select_numbers(numbers, threshold):
    selected_numbers = []
    for number in numbers:
        if number > threshold:
            selected_numbers.append(number)
    return selected_numbers

def is_palindrome(text):
    cleaned = text.lower().replace(' ', '')
    if not cleaned:
        return False
    return cleaned == cleaned[::-1]
