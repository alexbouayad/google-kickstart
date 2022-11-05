def max_points(first_task, second_task, k):
    n_first = len(first_task)
    n_second = len(second_task)
    result = 0

    k_pairs = [
        (x, k - x) for x in range(k + 1) if x <= n_first and k - x <= n_second
    ]

    for k_first, k_second in k_pairs:
        points_first = sum(first_task[:k_first])
        max_first = points_first

        for i in range(k_first):
            points_first -= first_task[k_first - 1 - i]
            points_first += first_task[n_first - 1 - i]
            max_first = max(max_first, points_first)

        points_second = sum(second_task[:k_second])
        max_second = points_second

        for i in range(k_second):
            points_second -= second_task[k_second - 1 - i]
            points_second += second_task[n_second - 1 - i]
            max_second = max(max_second, points_second)

        result = max(result, max_first + max_second)

    return result


if __name__ == "__main__":
    n_cases = int(input())

    for case in range(1, n_cases + 1):
        _ = input()
        first_task = list(map(int, input().split()))
        _ = input()
        second_task = list(map(int, input().split()))
        k = int(input())
        print(f"Case #{case}: {max_points(first_task, second_task, k)}")
