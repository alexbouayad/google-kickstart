MOD = int(1e9 + 7)
N_MAX = 400

modular_factorial = [1] * (N_MAX + 1)

for i in range(N_MAX):
    modular_factorial[i + 1] = (modular_factorial[i] * (i + 1)) % MOD


def extended_gcd(a, b):
    """Returns s, t, gcd(a, b) where s * a + t * b = gcd(a, b)."""
    s, u = 1, 0
    t, v = 0, 1

    while b:
        q, r = divmod(a, b)
        a, b = b, r
        s, u = u, s - q * u
        t, v = v, t - q * v

    return s, t, a


def modular_fraction(p, q):
    q_inverse, _, _ = extended_gcd(q, MOD)
    return (q_inverse * p) % MOD


def expected_candies(s):
    n = len(s)

    cache = [[[None] * n for _ in range(n)] for _ in range(n)]

    def palindromes(k, i, j):
        if j - i + 1 < k or k < 0:
            return 0

        if i == j or k == 0:
            return 1

        if cache[k][i][j] is not None:
            return cache[k][i][j]

        cache[k][i][j] = (
            (s[i] == s[j] and palindromes(k - 2, i + 1, j - 1))
            + palindromes(k, i, j - 1)
            + palindromes(k, i + 1, j)
            - palindromes(k, i + 1, j - 1)
        )
        cache[k][i][j] %= MOD

        return cache[k][i][j]

    candies = sum(
        modular_factorial[n - k]
        * modular_factorial[k]
        * palindromes(k, 0, n - 1)
        for k in range(n)
    )
    candies %= MOD

    return modular_fraction(candies, modular_factorial[n])


if __name__ == "__main__":
    n_cases = int(input())

    for case in range(1, n_cases + 1):
        _, s = input(), input()
        print(f"Case #{case}: {expected_candies(s)}")
