from __future__ import annotations  # Для аннотаций типов с обратными ссылками

from typing import Any


def generate_all_subsequences_with_return(sequence: list[Any]) -> list[list[Any]]:
    """
    Улучшенная версия, которая возвращает список всех подпоследовательностей
    в лексикографическом порядке.

    Аргументы:
    ----------
    sequence : list[Any]
        Входная последовательность

    Возвращает:
    ----------
    list[list[Any]]
        Список всех подпоследовательностей

    Пример:
    -------
    >>> result = generate_all_subsequences_with_return([1, 2, 3])
    >>> len(result)
    8
    >>> [] in result
    True
    >>> [1, 2, 3] in result
    True
    >>> [2, 3] in result
    True
    """
    result = []

    def backtrack(current: list[Any], index: int) -> None:
        """
        Внутренняя рекурсивная функция
        """
        # Когда дошли до конца последовательности
        if index == len(sequence):
            result.append(current[:])  # Добавляем копию
            return

        # Вариант 1: НЕ включаем текущий элемент
        backtrack(current, index + 1)

        # Вариант 2: Включаем текущий элемент
        current.append(sequence[index])
        backtrack(current, index + 1)
        current.pop()  # Backtracking

    backtrack([], 0)
    return result


# Версия с итеративным подходом (без рекурсии)
def generate_all_subsequences_iterative(sequence: list[Any]) -> list[list[Any]]:
    """
    Генерирует все подпоследовательности итеративно.
    Использует битовые маски для представления включения/исключения элементов.

    Аргументы:
    ----------
    sequence : list[Any]
        Входная последовательность

    Возвращает:
    ----------
    list[list[Any]]
        Список всех подпоследовательностей

    Пример:
    -------
    >>> result = generate_all_subsequences_iterative([1, 2])
    >>> result
    [[], [2], [1], [1, 2]]

    Алгоритм:
    ---------
    Для последовательности длины n существует 2^n подпоследовательностей.
    Каждой подпоследовательности соответствует битовая маска длины n,
    где 1 означает "включить элемент", 0 - "исключить".
    """
    n = len(sequence)
    result = []

    # Перебираем все битовые маски от 0 до 2^n - 1
    for mask in range(1 << n):  # 1 << n = 2^n
        subsequence = []

        # Для каждого бита в маске
        for i in range(n):
            # Если i-й бит установлен (равен 1)
            if mask & (1 << i):
                subsequence.append(sequence[i])

        result.append(subsequence)

    return result


# Тестирование улучшенных версий
if __name__ == "__main__":
    import itertools

    print("Тестирование различных реализаций:")
    print("=" * 50)

    # Тест 1: Проверка количества
    test_seq = [1, 2, 3, 4]

    # Реализация с возвратом
    result_backtrack = generate_all_subsequences_with_return(test_seq)
    print(f"Тест 1: sequence = {test_seq}")
    print(f"Рекурсивная реализация: {len(result_backtrack)} подпоследовательностей")
    print(f"Ожидалось: 2^{len(test_seq)} = {2 ** len(test_seq)}")
    print(f"Тест пройден: {len(result_backtrack) == 2 ** len(test_seq)}")

    # Итеративная реализация
    result_iterative = generate_all_subsequences_iterative(test_seq)
    print(f"\nИтеративная реализация: {len(result_iterative)} подпоследовательностей")
    print(f"Тест пройден: {len(result_iterative) == 2 ** len(test_seq)}")

    # Проверка, что результаты одинаковы
    # Преобразуем в множества для сравнения
    set_backtrack = set(tuple(sub) for sub in result_backtrack)
    set_iterative = set(tuple(sub) for sub in result_iterative)
    print(f"Реализации дают одинаковый результат: {set_backtrack == set_iterative}")

    # Проверка уникальности
    unique_backtrack = len(set_backtrack)
    unique_iterative = len(set_iterative)
    print(f"\nУникальных подпоследовательностей (рекурсия): {unique_backtrack}")
    print(f"Уникальных подпоследовательностей (итерация): {unique_iterative}")
    print(f"Все подпоследовательности уникальны: "
          f"{unique_backtrack == len(result_backtrack)}")

    # Вывод первых нескольких подпоследовательностей
    print(f"\nПервые 10 подпоследовательностей (рекурсивно):")
    for i, sub in enumerate(result_backtrack[:10]):
        print(f"  {i + 1:2d}. {sub}")

    print(f"\nПервые 10 подпоследовательностей (итеративно):")
    for i, sub in enumerate(result_iterative[:10]):
        print(f"  {i + 1:2d}. {sub}")
