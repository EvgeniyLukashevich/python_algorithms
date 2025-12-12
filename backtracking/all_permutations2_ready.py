def generate_all_permutations_with_return(sequence: list[int | str]) -> list[list[int | str]]:
    result = []
    index_used = [0] * len(sequence)

    def backtrack(current: list[int | str], index: int) -> None:
        if index == len(sequence):
            result.append(current[:])
            return

        for i in range(len(sequence)):
            if not index_used[i]:
                current.append(sequence[i])
                index_used[i] = 1
                backtrack(current, index + 1)
                current.pop()
                index_used[i] = 0

    backtrack([], 0)
    return result


# Тестирование улучшенной версии
if __name__ == "__main__":
    import itertools

    # Тест 1: Проверка количества
    test_seq = [1, 2, 3]
    permutations = generate_all_permutations_with_return(test_seq)
    expected_count = 3 * 2 * 1  # 3!
    print(f"Тест 1: sequence = {test_seq}")
    print(f"Получено перестановок: {len(permutations)}")
    print(f"Ожидалось: {expected_count}")
    print(f"Тест пройден: {len(permutations) == expected_count}")

    # Тест 2: Сравнение с itertools.permutations
    test_seq = ["A", "B", "C", "D"]
    our_result = generate_all_permutations_with_return(test_seq)
    itertools_result = list(itertools.permutations(test_seq))

    # Преобразуем кортежи itertools в списки для сравнения
    itertools_result_as_lists = [list(p) for p in itertools_result]

    print(f"\nТест 2: sequence = {test_seq}")
    print(f"Наш результат: {len(our_result)} перестановок")
    print(f"Itertools результат: {len(itertools_result)} перестановок")

    # Проверяем, что все перестановки уникальны
    unique_permutations = set(tuple(p) for p in our_result)
    print(f"Уникальных перестановок: {len(unique_permutations)}")
    print(f"Все перестановки уникальны: {len(unique_permutations) == len(our_result)}")

    # Проверяем соответствие с itertools
    our_set = set(tuple(p) for p in our_result)
    itertools_set = set(itertools_result)
    print(f"Результаты совпадают с itertools: {our_set == itertools_set}")
