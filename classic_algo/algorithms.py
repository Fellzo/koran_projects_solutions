def collatz_conjecture(number: int) -> int:
    """
    Гиппотеза Коллатца
    Найти кол-во шагов через которое f(number) = 1, если
    f(number) = f(number // 2) при четном number, иначе
    f(number) = f(number * 3 + 1)
    :param number: int Входное число
    :return: Количество шагов для достижения единицы
    :rtype: int
    :exception ValueError На вход подано отрицательное число или 0
    """
    if number < 1:
        raise ValueError("Входное число должно быть положительным")
    number_of_steps = 0
    while number != 1:
        if number % 2 == 0:
            number //= 2
        else:
            number = number * 3 + 1
        number_of_steps += 1
    return number_of_steps


def merge_sort(array: list, comparator: callable = lambda x: x) -> list:
    """
    Сортировка массива слиянием
    :param array: Входной массив
    :param comparator: Компоратор для сортировки (функция)
    :return: Отсортированный массив
    :rtype: list
    """

    def __merge(left: list, right: list) -> list:
        """
        Сливает два массива в один
        :param left: Первый массив
        :param right: Второй массив
        :return: Результирующий массив
        :rtype: list
        """
        res = []
        l, r = 0, 0
        while l < len(left) and r < len(right):
            if comparator(left[l]) < comparator(right[r]):
                res.append(left[l])
                l += 1
            else:
                res.append(right[r])
                r += 1
        return res + left[l:] + right[r:]

    if len(array) <= 1:
        return array
    return __merge(merge_sort(array[:len(array) // 2]), merge_sort(array[len(array) // 2:]))


def bubble_sort(array: list, comparator: callable = lambda x: x) -> list:
    """
    Сортировка массива пузырьком
    :param array: Входной массив
    :param comparator: Компоратор для сортировки (функция)
    :return: Отсортированный массив
    :rtype: list
    """
    res = list(array)   # Для сохранения входного массива в исходном состоянии
    f = True
    while f:
        f = False
        for i in range(len(res) - 1):
            if comparator(res[i]) > comparator(res[i + 1]):
                f = True
                res[i], res[i + 1] = res[i + 1], res[i]
    return res


def sieve_of_eratosthenes(number: int) -> list:
    """
    Решето Эратосфена
    :param number
    :return: Список простых чисел от 2 до number
    :exception: ValueError: Если на вход подано число меньше 1
    """
    if number < 1:
        raise ValueError('Входное число должно быть положительным')
    res = [0] * (number + 1)
    primes = []
    for i in range(2, number):
        if res[i] == 0:
            primes.append(i)
            for j in range(i * 2, number, i):
                res[j] = 1
    return primes


def is_prime_number(number: int) -> bool:
    """
    Проверка числа на простоту за O(sqrt(number))
    :param number:
    :return: True если число простое, False иначе
    :exception: ValueError: Если на вход подано число меньше 1
    """
    if number < 1:
        raise ValueError('Входное число должно быть положительным')
    d = 2
    while d * d <= number:
        if number % d == 0:
            return False
        d += 1
    return number != 1
