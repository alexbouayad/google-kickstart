from collections import defaultdict
from heapq import heappop, heappush

n_cases = int(input())

for case in range(1, n_cases + 1):
    n_days, n_species, day_capacity = map(int, input().split())
    seeds = defaultdict(list)

    for _ in range(n_species):
        quantity, maturation, value = map(int, input().split())
        seeds[maturation].append((value, quantity))

    maturation_lst = sorted(seeds.keys())
    maturation_lst.append(n_days)
    maturation_lst = [
        (a, day_capacity * (b - a))
        for a, b in zip(maturation_lst[:-1], maturation_lst[1:])
    ]

    count = 0
    heap = []

    for day, capacity in maturation_lst:
        for value, quantity in seeds[day]:
            heappush(heap, (-value, quantity))

        while heap and capacity:
            value_neg, quantity = heappop(heap)
            n_planted = min(capacity, quantity)
            quantity -= n_planted
            capacity -= n_planted

            if quantity:
                heappush(heap, (value_neg, quantity))

            count -= n_planted * value_neg

    print(f"Case #{case}: {count}")
