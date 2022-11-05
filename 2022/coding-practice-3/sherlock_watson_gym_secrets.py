from collections import defaultdict

N_MOD = int(1e9 + 7)

n_cases = int(input())

def mod_power(i, a, k):
    if a == 0:
        return 1

    if a == 1:
        return i % k

    result = (mod_power(i, a // 2, k) ** 2) % k
    return (result * i) % k if a % 2 else result

for case in range(1, n_cases + 1):
    a, b, n, k = map(int, input().split())

    def count(n, m):
        n_a_powers = defaultdict(int)

        for i in range(1, n + 1):
            n_a_powers[mod_power(i, a, k)] += 1

        result = 0

        for j in range(1, m + 1):
            x = (- mod_power(j, b, k)) % k
            result += n_a_powers[x]
            result -= 1 if (mod_power(j, a, k) - x) % k == 0 else 0

        return result % N_MOD

    q, r = divmod(n, k)
    q %= N_MOD

    if k == 1:
        result = n * (n - 1) % N_MOD

    else:
        result = 0
        result += (q ** 2) * count(k, k) if q else 0
        result %= N_MOD
        result += q * count(k, r) if q else 0
        result %= N_MOD
        result += q * count(r, k) if q else 0
        result %= N_MOD
        result += count(r, r)
        result %= N_MOD

    print(f"Case #{case}: {result}")
