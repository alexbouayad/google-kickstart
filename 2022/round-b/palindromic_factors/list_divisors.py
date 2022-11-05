from math import ceil

n_cases = int(input())


def is_palindrome(x):
    x = str(x)
    n = len(x)
    return all(x[i] == x[n - 1 - i] for i in range(n // 2 + 1))


for case in range(1, n_cases + 1):
    a = int(input())
    a_sqrt = ceil(a**0.5)

    divisors = set.union(
        *({b, a // b} for b in range(1, a_sqrt + 1) if a % b == 0)
    )
    result = sum(is_palindrome(b) for b in divisors)
    print(f"Case #{case}: {result}")
