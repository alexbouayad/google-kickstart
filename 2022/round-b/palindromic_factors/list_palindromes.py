n_cases = int(input())
palindromes = [[], list(range(1, 10)), [d * 11 for d in range(1, 10)]]

for case in range(1, n_cases + 1):
    a = input()
    n = len(a)
    a = int(a)
    i = len(palindromes)

    while i <= n:
        palindromes.append(
            [
                d * 10 ** (i - 1) + b * 10 ** ((i - m) // 2) + d
                for m in range(i - 2, 0, -2)
                for b in palindromes[m] + [0]
                for d in range(1, 10)
            ]
        )
        i += 1

    result = sum(
        a % b == 0 for m in range(1, n + 1) for b in palindromes[m] if b
    )
    print(f"Case #{case}: {result}")
