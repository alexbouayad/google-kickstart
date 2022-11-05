n_cases = int(input())

for case in range(1, n_cases + 1):
    n, d = map(int, input().split())
    padlock = list(map(int, input().split()))

    result = [[[0, 0] for _ in range(n + 1)] for _ in range(n + 1)]

    for m in range(n + 1):
        for i in range(n - m):
            j = i + m

            for direction in range(2):
                idx = i - 1 if direction == 0 else j + 1
                base = padlock[idx] if 0 <= idx < n else 0
                distance_left = abs(padlock[i] - base)
                distance_right = abs(padlock[j] - base)
                distance_left = min(distance_left, d - distance_left)
                distance_right = min(distance_right, d - distance_right)

                result[i][j][direction] = min(
                    distance_left + result[i + 1][j][0],
                    distance_right + result[i][j - 1][1],
                )

    print(f"Case #{case}: {result[0][n - 1][1]}")
