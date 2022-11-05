from collections import defaultdict

n_cases = int(input())

for case in range(1, n_cases + 1):
    n, q = map(int, input().split())
    edges = defaultdict(set)

    for _ in range(n - 1):
        i, j = map(int, input().split())
        edges[i].add(j)
        edges[j].add(i)

    for _ in range(q):
        input()

    n_containers = defaultdict(int)
    stack = [(1, 1)]
    visited = set()

    while stack:
        i, level = stack.pop()
        n_containers[level] += 1
        visited.add(i)
        stack += [
            (j, level + 1) for j in edges[i]
            if j not in visited
        ]

    level = 1
    capacity = 1
    count = 0

    for _ in range(q):
        capacity -= 1

        if capacity <= 0:
            count += n_containers[level]
            level += 1
            capacity += n_containers[level]

    print(f"Case #{case}: {count}")
