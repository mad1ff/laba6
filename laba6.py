import re
import fnmatch


# ЗАДАЧА 1: КОМБИНАТОРИКА
class CombinatoricsCounter:
    def __init__(self, alphabet, length, first_char, last_char):
        self.alphabet = alphabet
        self.length = length
        self.first_char = first_char
        self.last_char = last_char

    def count_sequences(self):
        if self.length < 2:
            return 0
        return len(self.alphabet) ** (self.length - 2)


# ЗАДАЧА 2: СИСТЕМЫ СЧИСЛЕНИЯ
class BaseConverter:
    def __init__(self, expression, base):
        self.expression = expression
        self.base = base

    def evaluate(self):
        return eval(self.expression)

    def count_unique_digits(self):
        value = self.evaluate()
        if value == 0:
            return 1
        digits = set()
        temp = abs(value)
        while temp > 0:
            digits.add(temp % self.base)
            temp //= self.base
        return len(digits)


# ЗАДАЧА 3: ПОИСК ПО МАСКЕ И ДЕЛИМОСТИ
class MaskDivisibleFinder:
    def __init__(self, mask, divisor, max_value):
        self.mask = mask
        self.divisor = divisor
        self.max_value = max_value
        self.regex = fnmatch.translate(mask)
        self.pattern = re.compile(self.regex)

    def matches_mask(self, num_str):
        return bool(self.pattern.fullmatch(num_str))

    def find_numbers(self):
        results = []
        for num in range(self.divisor, self.max_value + 1, self.divisor):
            if self.matches_mask(str(num)):
                results.append((num, num // self.divisor))
        return results


# ЗАПУСК И ВЫВОД РЕЗУЛЬТАТОВ
if __name__ == "__main__":
    import doctest
    doctest.testmod()

    # ЗАДАЧА 1
    task1 = CombinatoricsCounter(['K', 'A', 'T', 'E', 'P'], 6, 'P', 'K')
    print(f"Задача 1: {task1.count_sequences()}")

    # ЗАДАЧА 2
    task2 = BaseConverter("216**6 + 216**4 + 36**6 - 6**14 - 24", 6)
    print(f"Задача 2: {task2.count_unique_digits()}")

    # ЗАДАЧА 3
    task3 = MaskDivisibleFinder("12345??8", 23, 10**9)
    results = task3.find_numbers()
    print(f"Задача 3: найдено {len(results)} чисел")
    for num, quot in results:
        print(f"  {num} -> {quot}")
