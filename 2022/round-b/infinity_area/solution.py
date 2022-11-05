from math import pi

n_cases = int(input())

for case in range(1, n_cases + 1):
    r, a, b = map(int, input().split())
    area = r**2

    while r:
        r *= a
        area += r**2
        r //= b
        area += r**2

    area *= pi
    print(f"Case #{case}: {area}")
