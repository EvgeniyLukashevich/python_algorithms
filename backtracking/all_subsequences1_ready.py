from typing import Any


def generate_all_subsequences(sequence: list[Any]) -> None:
    create_state_space_tree(sequence, [], 0)


def create_state_space_tree(
        sequence: list[Any],
        current_subsequence: list[Any],
        index: int
) -> None:
    if index == len(sequence):
        print(current_subsequence)
        return

    create_state_space_tree(sequence, current_subsequence, index + 1)
    current_subsequence.append(sequence[index])
    create_state_space_tree(sequence, current_subsequence, index + 1)
    current_subsequence.pop()


if __name__ == "__main__":
    print("Пример 1: Числовая последовательность")
    print("=" * 40)
    seq: list[Any] = [1, 2, 3]
    print(f"Исходная последовательность: {seq}")
    print(f"Ожидаемое количество подпоследовательностей: 2^{len(seq)} = {2 ** len(seq)}")
    print("Все подпоследовательности (в обратном порядке из-за реализации):")
    generate_all_subsequences(seq)

    print("\n" + "=" * 40 + "\n")

    print("Пример 2: Строковая последовательность")
    print("=" * 40)
    seq.clear()  # Очищаем список
    seq.extend(["A", "B", "C"])  # Добавляем новые элементы
    print(f"Исходная последовательность: {seq}")
    print(f"Ожидаемое количество подпоследовательностей: 2^{len(seq)} = {2 ** len(seq)}")
    print("Все подпоследовательности:")
    generate_all_subsequences(seq)
