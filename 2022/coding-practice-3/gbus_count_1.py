n_cases = int(input())

for case in range(1, n_cases + 1):
    input()
    bus_ranges = list(map(int, input().split()))
    bus_ranges = list(zip(bus_ranges[::2], bus_ranges[1::2]))
    n_cities = int(input())
    cities = [int(input()) for _ in range(n_cities)]

    if case < n_cases:
        input()

    n_served = [sum(a <= city <= b for a, b in bus_ranges) for city in cities]
    print(f"Case #{case}:", end=" ")
    print(*n_served, sep=" ")
