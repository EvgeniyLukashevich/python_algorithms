def generate_all_permutations(sequence: list[int | str]) -> None:
    index_used = [0 for i in range(len(sequence))]
    create_state_space_tree(sequence, [], 0, index_used)


def create_state_space_tree(
        sequence: list[int | str],
        current_sequence: list[int | str],
        index: int,
        index_used: list[int],
) -> None:
    if index == len(sequence):
        print(current_sequence)
        return
    for i in range(len(sequence)):
        if not index_used[i]:
            current_sequence.append(sequence[i])
            index_used[i] = 1
            create_state_space_tree(sequence, current_sequence, index + 1, index_used)
            current_sequence.pop()
            index_used[i] = 0


# Демонстрация работы алгоритма
if __name__ == "__main__":
    print("Пример 1: Числовая последовательность")
    print("=_" * 22)
    sequence: list[int | str] = [3, 1, 2, 4]
    print(f"Исходная последовательность: {sequence}")
    print(f"Ожидаемое количество перестановок: 4! = {4 * 3 * 2 * 1}")
    print("Все перестановки:")
    generate_all_permutations(sequence)

    print("\n" + "=" * 44 + "\n" + "=" * 44 + "\n")

    print("Пример 2: Строковая последовательность")
    print("=_" * 22)
    sequence_2: list[int | str] = ["A", "B", "C"]
    print(f"Исходная последовательность: {sequence_2}")
    print(f"Ожидаемое количество перестановок: 3! = {3 * 2 * 1}")
    print("Все перестановки:")
    generate_all_permutations(sequence_2)
