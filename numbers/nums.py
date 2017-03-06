def factorial(x: int) -> int:
    """
    Нахождение факториала числа
    x! = 1*2*3*...*x
    :param x: Входное число
    :return: Факториал числа
    """
    if x < 0:
        raise ValueError('Входное число должно быть больше или равно 0')
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
    """
    if curr_base not in range(2, 37) or required_base not in range(2, 37):
        raise ValueError('Основание системы счисления должно быть в интервале от 2 до 36')
    if not number:
        raise ValueError('На вход получена пустая строка')
    if number[0] == '-':
        raise NotImplementedError('Отрицательные числа не поддерживаются')
    number = number.upper()
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
        if digit_val > max_digit:
            raise ValueError('Неверный символ %s для сисстемы счисления с основанием %s' % (digit_val, curr_base))
    res = number[::-1]
    curr_val = 0
    # Перевод числа в десятичную СС
    for i in range(len(res)):
        curr_val += curr_base ** i * int(res[i])

    res = ''
    while curr_val > 0:
        remainder = curr_val % required_base
        if remainder > 10:
            remainder = chr(ord('A') + remainder - 10)
        res += str(remainder)
        curr_val //= required_base
    return res[::-1]