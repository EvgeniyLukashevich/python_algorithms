from typing import Any


def generate_all_subsequences_with_return(sequence: list[Any]) -> list[list[Any]]:
    result = []

    def backtrack(current: list[Any], index: int) -> None:
        if index == len(sequence):
            result.append(current[:])
            return

        backtrack(current, index + 1)
        current.append(sequence[index])
        backtrack(current, index + 1)
        current.pop()

    backtrack([], 0)
    return result


def generate_all_subsequences_iterative(sequence: list[Any]) -> list[list[Any]]:
    n = len(sequence)
    result = []

    for mask in range(1 << n):
        subsequence = []

        for i in range(n):
            if mask & (1 << i):
                subsequence.append(sequence[i])

        result.append(subsequence)

    return result


if __name__ == "__main__":

    print("Тестирование различных реализаций:")
    print("=" * 50)

    test_seq = [1, 2, 3, 4]

    result_backtrack = generate_all_subsequences_with_return(test_seq)
    print(f"Тест 1: sequence = {test_seq}")
    print(f"Рекурсивная реализация: {len(result_backtrack)} подпоследовательностей")
    print(f"Ожидалось: 2^{len(test_seq)} = {2 ** len(test_seq)}")
    print(f"Тест пройден: {len(result_backtrack) == 2 ** len(test_seq)}")

    result_iterative = generate_all_subsequences_iterative(test_seq)
    print(f"\nИтеративная реализация: {len(result_iterative)} подпоследовательностей")
    print(f"Тест пройден: {len(result_iterative) == 2 ** len(test_seq)}")

    set_backtrack = set(tuple(sub) for sub in result_backtrack)
    set_iterative = set(tuple(sub) for sub in result_iterative)
    print(f"Реализации дают одинаковый результат: {set_backtrack == set_iterative}")

    unique_backtrack = len(set_backtrack)
    unique_iterative = len(set_iterative)
    print(f"\nУникальных подпоследовательностей (рекурсия): {unique_backtrack}")
    print(f"Уникальных подпоследовательностей (итерация): {unique_iterative}")
    print(f"Все подпоследовательности уникальны: "
          f"{unique_backtrack == len(result_backtrack)}")

    print(f"\nПервые 10 подпоследовательностей (рекурсивно):")
    for i, sub in enumerate(result_backtrack[:10]):
        print(f"  {i + 1:2d}. {sub}")

    print(f"\nПервые 10 подпоследовательностей (итеративно):")
    for i, sub in enumerate(result_iterative[:10]):
        print(f"  {i + 1:2d}. {sub}")
