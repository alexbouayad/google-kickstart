t = int(input())

for case_id in range(1, t + 1):
    n = int(input())
    visits = list(map(int, input().split()))
    visits.append(-1)
    max_visits = -1
    n_records = 0

    for j in range(n):
        if max_visits < visits[j] and visits[j + 1] < visits[j]:
            n_records += 1

        max_visits = max(max_visits, visits[j])

    print(f"Case #{case_id}: {n_records}")
