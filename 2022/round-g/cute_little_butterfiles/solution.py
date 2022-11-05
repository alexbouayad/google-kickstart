def cute_little_butterflies(flowers, e_turn):
    print()
    print(flowers)

    n = len(flowers)
    flowers.sort(key=lambda x: (x[1], x[0]))

    levels = []
    i = 0

    while i < n:
        lst = [(flowers[i][0], flowers[i][-1])]
        i += 1

        while i < n and flowers[i][1] == flowers[i - 1][1]:
            lst.append((flowers[i][0], flowers[i][-1]))
            i += 1

        levels.append(lst)

    levels.append([(float("inf"), 0)])
    print(levels)
    n_levels = len(levels)
    nearest_left, nearest_right = {}, {}

    for i in range(n_levels):
        for x, _ in levels[i]:
            j = i - 1

            while j >= 0 and x < levels[j][0][0]:
                j = nearest_left[j, x]

            nearest_left[i] = j

    for i in range(n_levels):
        for x, _ in levels[i]:
            j = i - 1

            while j >= 0 and levels[j][-1][0] < x:
                j = nearest_right[j]

            nearest_right[i] = j

    nearest = nearest_left, nearest_right

    print(nearest)
    cache = {}

    def solve(direction, i, x):
        if i < 0:
            return 0

        if (direction, i, x) in cache:
            return cache[direction, i, x]

        j = nearest[direction][i]
        cache[direction, i, x] = solve(direction, j, x)
        energy = 0

        if direction == 0:
            s = 0

            while s + 1 < len(levels[j]) and levels[j][s + 1][0] <= x:
                s += 1

        else:
            s = len(levels[j]) - 1

            while s > 0 and x <= levels[j][s - 1][0]:
                s -= 1

        k = s

        while 0 <= k < len(levels[j]):
            y = levels[j][k][0]
            energy += levels[j][k][1]

            cache[direction, i, x] = max(
                cache[direction, i, x],
                energy + solve(direction, j, y),
                energy - e_turn + solve(1 - direction, j, y),
            )

            k -= 1 if direction == 0 else -1

        k = s + 1 if direction else s - 1
        energy -= e_turn

        while 0 <= k < len(levels[j]):
            y = levels[j][k][0]
            energy += levels[j][k][1]

            cache[direction, i, x] = max(
                cache[direction, i, x],
                energy + solve(1 - direction, j, y),
                energy - e_turn + solve(direction, j, y),
            )

            k += 1 if direction == 0 else -1

        return cache[direction, i, x]

    return solve(1, n_levels - 1, float("inf"))


if __name__ == "__main__":
    n_cases = int(input())
    import sys

    sys.setrecursionlimit(10000000)

    for case in range(1, n_cases + 1):
        n, e_turn = map(int, input().split())
        flowers = [tuple(map(int, input().split())) for _ in range(n)]
        print(f"Case #{case}:", cute_little_butterflies(flowers, e_turn))
