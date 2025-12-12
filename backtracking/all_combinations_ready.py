from __future__ import annotations

def generate_all_combinations(n: int, k: int) -> list[list[int]]:
    if k < 0:
        raise ValueError("k must not be negative")
    if n < 0:
        raise ValueError("n must not be negative")

    result: list[list[int]] = []
    create_all_state(1, n, k, [], result)

    return result


def create_all_state(
        increment: int,
        total_number: int,
        level: int,
        current_list: list[int],
        total_list: list[list[int]],
) -> None:
    if level == 0:
        total_list.append(current_list[:])
        return

    for i in range(increment, total_number - level + 2):
        current_list.append(i)
        create_all_state(i + 1, total_number, level - 1, current_list, total_list)
        current_list.pop()


if __name__ == "__main__":
    n: int = int(input("Введите общее количество элементов: "))
    k: int = int(input("Введите количество элементов в комбинации: "))

    result_list: list[list[int]] = generate_all_combinations(n, k)

    print(f"\nОбщее количество элементов: {n}\n"
          f"Элементов в комбинации: {k}\n"
          f"Количество комбинаций: {len(result_list)}\n"
          f"РЕЗУЛЬТАТ:")

    for j in range(0, len(result_list), 5):  # от 0 до длины списка с шагом 5
        chunk = result_list[j:j + 5]
        # на первой итерации в chunk запишутся элементы result[0]-result[4]
        # на второй - result[5]-result[9] и т.д.
        print(chunk)
