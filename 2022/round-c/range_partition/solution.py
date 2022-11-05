def partition(n, x, y):
    q, r = divmod(n * (n + 1) / 2, x + y)

    if r:
        return []

    x *= q
    i = 1

    while x >= 0:
        x -= i
        i += 1

    return [k for k in range(1, i) if k != -x]


if __name__ == "__main__":
    n_cases = int(input())

    for case in range(1, n_cases + 1):
        n, x, y = map(int, input().split())
        lst = partition(n, x, y)

        if lst:
            print(f"Case #{case}: POSSIBLE")
            print(len(lst))
            print(*lst)

        else:
            print(f"Case #{case}: IMPOSSIBLE")
