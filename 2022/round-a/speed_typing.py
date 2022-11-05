n_cases = int(input())

for case in range(1, n_cases + 1):
    i_string = input()
    p_string = input()
    deletions = 0
    i_idx, p_idx = 0, 0

    while i_idx < len(i_string) and p_idx < len(p_string):
        while p_idx < len(p_string) and i_string[i_idx] != p_string[p_idx]:
            p_idx += 1
            deletions += 1

        i_idx += 1
        p_idx += 1

    remainder = len(p_string) - deletions - len(i_string)
    result = deletions + remainder if remainder >= 0 else "IMPOSSIBLE"
    print(f"Case #{case}: {result}")
