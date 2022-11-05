n_cases = int(input())

for case in range(1, n_cases + 1):
    n, d = map(int, input().split())
    padlock = list(map(int, input().split()))
    padlock.append(0)

    result = [[[None, None] for _ in range(n)] for _ in range(n)]

    def solve(i, j, direction):
        if j < i:
            return 0

        if result[i][j][direction] is not None:
            return result[i][j][direction]

        base = padlock[i - 1 if direction == 0 else j + 1]
        distance_left = abs(padlock[i] - base)
        distance_right = abs(padlock[j] - base)
        distance_left = min(distance_left, d - distance_left)
        distance_right = min(distance_right, d - distance_right)

        result[i][j][direction] = min(
            distance_left + solve(i + 1, j, 0),
            distance_right + solve(i, j - 1, 1),
        )

        return result[i][j][direction]

    print(f"Case #{case}: {solve(0, n - 1, 1)}")
