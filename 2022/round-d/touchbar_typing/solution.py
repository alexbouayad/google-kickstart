def minimal_time(word, keyboard):
    n_keys = len(keyboard)
    result = [[0] * len(keyboard) for _ in range(2)]

    for i, key in enumerate(word):
        key_prev, key_next = [None] * n_keys, [None] * n_keys
        j_prev, j_next = None, None

        for j in range(n_keys):
            if keyboard[j] == key:
                j_prev = j

            key_prev[j] = j_prev

        for j in reversed(range(n_keys)):
            if keyboard[j] == key:
                j_next = j

            key_next[j] = j_next

        for j in range(n_keys):
            times = []

            if key_prev[j] is not None:
                j_prev = key_prev[j]
                times.append(result[(i + 1) % 2][j_prev] + abs(j - j_prev))

            if key_next[j] is not None:
                j_next = key_next[j]
                times.append(result[(i + 1) % 2][j_next] + abs(j - j_next))

            result[i % 2][j] = min(times)

    return min(result[i % 2])


if __name__ == "__main__":
    n_cases = int(input())

    for case in range(1, n_cases + 1):
        _ = input()
        word = list(map(int, input().split()))
        _ = input()
        keyboard = list(map(int, input().split()))
        print(f"Case #{case}: {minimal_time(word, keyboard)}")
