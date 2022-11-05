from collections import Counter
from math import factorial

n_cases = int(input())


def counter_total(x):
    return len(list(x.elements()))


def orbit_size(x):
    result = factorial(counter_total(x))

    for m in x.values():
        result //= factorial(m)

    return result


def n_more_than_or_equal(x, a):
    n = counter_total(x)

    if n < len(a):
        return 0

    a = [0] * (n - len(a)) + a

    def helper(j):
        if j == n:
            return 1

        count = 0
        d_range = [d for d in range(a[j] if (j or a[j]) else 1, 10) if x[d]]

        for d in d_range:
            x[d] -= 1
            count += helper(j + 1) if d == a[j] else orbit_size(x)
            x[d] += 1

        return count

    return helper(0)


def n_interesting_between(x, a, b):
    interesting = False
    sum_digits = sum(x.elements())
    product = 1

    for d in x.elements():
        product *= d
        product %= sum_digits

        if not product:
            interesting = True
            break

    return (
        n_more_than_or_equal(x, a)
        - n_more_than_or_equal(x, b)
        + all(x[d] == Counter(b)[d] for d in range(10))
        if interesting
        else 0
    )


for case in range(1, n_cases + 1):
    a, b = map(list, input().split())
    a, b = list(map(int, a)), list(map(int, b))

    def helper(x, d):
        if d == 10:
            return (
                n_interesting_between(x, a, b)
                if any(x.elements()) and len(a) <= counter_total(x)
                else 0
            )

        count = 0

        for i in range(len(b) - counter_total(x) + 1):
            x[d] = i
            count += helper(x, d + 1)
            x[d] = 0

        return count

    print(f"Case #{case}: {helper(Counter(), 0)}")
