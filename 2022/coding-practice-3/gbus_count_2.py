from calendar import c
from collections import Counter, defaultdict

n_cases = int(input())

for case in range(1, n_cases + 1):
    input()
    bus_ranges = list(map(int, input().split()))
    n_cities = int(input())
    cities_lst = [int(input()) for _ in range(n_cities)]

    if case < n_cases:
        input()

    start = Counter(bus_ranges[::2])
    end = Counter(bus_ranges[1::2])

    n_served = {}
    count = 0
    city = 1
    cities_set = set(cities_lst)

    while cities_set:
        count += start[city]
        count -= end[city - 1]

        if city in cities_set:
            n_served[city] = count
            cities_set.remove(city)

        city += 1

    print(f"Case #{case}:", end=" ")
    print(*(n_served[city] for city in cities_lst), sep=" ")
