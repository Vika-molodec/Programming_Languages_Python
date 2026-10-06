def is_prime(n):
    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 1
    return True
for number in (2, 9, 17, 49):
    print(number, is_prime(number))
