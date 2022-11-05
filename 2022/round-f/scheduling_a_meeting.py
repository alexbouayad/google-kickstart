from collections import defaultdict

n_cases = int(input())

for case in range(1, n_cases + 1):
    n_tls, k, window_length, calendar_length = map(int, input().split())
    n_meetings = int(input())
    meetings_start, meetings_end = defaultdict(list), defaultdict(list)

    for _ in range(n_meetings):
        i, a, b = map(int, input().split())
        meetings_start[a].append(i - 1)
        meetings_end[b].append(i - 1)

    min_sum_k = float("inf")
    meetings = [0] * n_tls
    n_tls_lst = [n_tls if i == 0 else 0 for i in range(n_meetings + 1)]
    max_k = 0
    n_max_k = k
    sum_k = 0
    window_end = calendar_length + window_length

    while window_length <= window_end:
        window_start = window_end - window_length

        for i in meetings_end[window_start + 1]:
            meetings[i] += 1

            if meetings[i] < max_k:
                sum_k += 1

            elif meetings[i] == max_k:
                n_max_k += 1
                sum_k += 1

            elif meetings[i] == max_k + 1 and n_max_k == n_tls_lst[max_k]:
                max_k += 1
                n_max_k = 1
                sum_k += 1

            n_tls_lst[meetings[i]] += 1
            n_tls_lst[meetings[i] - 1] -= 1

        for i in meetings_start[window_end]:
            meetings[i] -= 1
            n_tls_lst[meetings[i]] += 1
            n_tls_lst[meetings[i] + 1] -= 1

            if meetings[i] < max_k - 1:
                sum_k -= 1

            if meetings[i] == max_k - 1:
                n_max_k -= 1
                sum_k -= 1

                if n_max_k == 0:
                    max_k -= 1
                    n_max_k = n_tls_lst[max_k]

        if window_end <= calendar_length:
            min_sum_k = min(min_sum_k, sum_k)

        window_end -= 1

    print(f"Case #{case}: {min_sum_k}")
