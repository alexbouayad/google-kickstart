t = int(input())

for case_id in range(1, t + 1):
    _, n_kids = map(int, input().split())
    n_candies = sum(map(int, input().split()))
    print(f"Case #{case_id}: {n_candies % n_kids}")
