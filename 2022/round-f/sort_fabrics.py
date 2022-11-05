n_cases = int(input())

for case in range(1, n_cases + 1):
    n_fabrics = int(input())
    colours = []
    durabilities = []
    uids = []

    for _ in range(n_fabrics):
        c, d, u = input().split()
        d, u = int(d), int(u)
        colours.append(c)
        durabilities.append(d)
        uids.append(u)

    colours = list(zip(colours, uids))
    durabilities = list(zip(durabilities, uids))
    colours.sort()
    durabilities.sort()

    count = sum(u == v for (_, u), (_, v) in zip(colours, durabilities))
    print(f"Case #{case}: {count}")
