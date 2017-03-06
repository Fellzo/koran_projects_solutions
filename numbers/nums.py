def factorial(x: int) -> int:
    """
    Нахождение факториала числа
    x! = 1 * 2 * 3 * ... * x

    :param x: Входное число
    :return: Факториал числа

    >>> factorial(0)
    1

    >>> factorial(5)
    120

    >>> factorial(10)
    3628800

    >>> factorial(-1)
    Traceback (most recent call last):
     ...
    ValueError: Входное число должно быть >= 0
    """
    if x < 0:
        raise ValueError('Входное число должно быть >= 0')
    if x == 0:
        return 1
    return x * factorial(x - 1)


def converter(number: str, curr_base: int, required_base: int) -> str:
    """
    Перевод числа number из системы счисления с основанием curr_base в систему счисления с основанием required_base

    :param number: Входное число
    :param curr_base: Исходная система счисления
    :param required_base: Требуемая система счисления
    :return: Переведенное число

    >>> converter('1111', 2, 10)
    '15'

    >>> converter('F', 16, 10)
    '15'

    >>> converter('7182', 13, 5)
    '1000104'

    >>> converter('ZZ', 3, 10)
    Traceback (most recent call last):
    ...
    ValueError: Неверный символ 35 для системы счисления с основанием 3
    """
    if curr_base not in range(2, 37) or required_base not in range(2, 37):
        raise ValueError('Основание системы счисления должно быть в интервале от 2 до 36')
    if not number:
        raise ValueError('На вход получена пустая строка')
    positive = number[0] != '-'
    number = number.upper().replace('-', '')
    if curr_base < 10:
        max_digit = curr_base
    else:
        max_digit = ord('A') + curr_base - 10
    for digit in number:
        if not digit.isalnum():
            raise ValueError('Число должно состоять только из букв и цифр')
        if digit.isalpha():
            digit_val = ord(digit) - ord('A') + 10
        else:
            digit_val = int(digit)
        if digit_val >= max_digit:
            raise ValueError('Неверный символ %s для системы счисления с основанием %s' % (digit_val, curr_base))
    res = number[::-1]
    curr_val = 0
    # Перевод числа в десятичную СС
    for i in range(len(res)):
        curr_val += curr_base ** i * int(res[i], curr_base)

    res = ''
    while curr_val > 0:
        remainder = curr_val % required_base
        if remainder > 10:
            remainder = chr(ord('A') + remainder - 10)
        res += str(remainder)
        curr_val //= required_base
    if not positive:
        res += '-'
    return res[::-1]


def fibonacci_sequence(number: int) -> list:
    """
    Генерирует number первых членов последовательности Фибоначчи
    fib[0] = 0
    fib[1] = 1
    fib[i] = fib[i - 1] + fib[i - 2], при i > 2

    :param number:
    :return: Список из number членов последовательности Фибоначчи
    :exception: ValueError Если кол-во членов отрицательно

    >>> fibonacci_sequence(0)
    []

    >>> fibonacci_sequence(3)
    [0, 1, 1]

    >>> fibonacci_sequence(5)
    [0, 1, 1, 2, 3]

    >>> fibonacci_sequence(-1)
    Traceback (most recent call last):
     ...
    ValueError: Количество члено последовательности должен быть положительным
    """
    result = [0, 1]
    if number < 0:
        raise ValueError('Количество члено последовательности должен быть положительным')
    for i in range(2, number):
        result.append(result[-1] + result[-2])
    return result[:number]