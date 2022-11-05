MOD = int(1e9 + 7)
N_MAX = 400

mod_factorial = [1] * (N_MAX + 1)
mod_inverse = [1] * (N_MAX + 1)
mod_factorial_inv = [1] * (N_MAX + 1)


for i in range(2, N_MAX + 1):
    mod_factorial[i] = mod_factorial[i - 1] * i % MOD
    mod_inverse[i] = -mod_inverse[MOD % i] * (MOD // i) % MOD
    mod_factorial_inv[i] = mod_factorial_inv[i - 1] * mod_inverse[i] % MOD


def expected_candies(s):
    n = len(s)
    candies = 0
    count = [[[0] * n for _ in range(n)] for _ in range(3)]

    for k in range(1, n):
        for i in reversed(range(n)):
            count[k % 3][i][i] = 1 if k == 1 else 0

            for j in range(i + 1, n):
                count[k % 3][i][j] = 0

                if s[i] == s[j] and k == 2:
                    count[k % 3][i][j] += 1

                elif s[i] == s[j] and k > 2:
                    count[k % 3][i][j] += count[(k - 2) % 3][i + 1][j - 1]

                count[k % 3][i][j] += count[k % 3][i][j - 1]
                count[k % 3][i][j] += count[k % 3][i + 1][j]
                count[k % 3][i][j] -= count[k % 3][i + 1][j - 1]
                count[k % 3][i][j] %= MOD

        candies += (
            mod_factorial[n - k] * mod_factorial[k] * count[k % 3][0][n - 1]
        )
        candies %= MOD

    return (candies * mod_factorial_inv[n] + 1) % MOD


if __name__ == "__main__":
    n_cases = int(input())

    for case in range(1, n_cases + 1):
        _, s = input(), input()
        print(f"Case #{case}: {expected_candies(s)}")
