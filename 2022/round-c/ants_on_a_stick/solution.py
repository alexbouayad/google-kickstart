def order(ants, n_ants, length):
    indices = sorted(range(n_ants), key=lambda i: ants[i])
    lefts = [ants[i] for i in indices if ants[i][1] == 0]
    rights = [ants[i] for i in indices if ants[i][1] == 1]

    distances = sorted(
        (position if direction == 0 else length - position, idx)
        for idx, (position, direction) in zip(indices, lefts + rights)
    )
    return [i + 1 for _, i in distances]


if __name__ == "__main__":
    n_cases = int(input())

    for case in range(1, n_cases + 1):
        n_ants, length = map(int, input().split())
        ants = [tuple(map(int, input().split())) for _ in range(n_ants)]
        print(f"Case #{case}:", end=" ")
        print(*order(ants, n_ants, length))
