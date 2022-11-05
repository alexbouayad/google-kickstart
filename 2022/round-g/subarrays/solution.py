def subarrays(array, n):
    prefix = [0]
    prefix.extend(prefix[-1] + array[i] for i in range(n))

    second_prefix = [0]
    second_prefix.extend(second_prefix[-1] + prefix[i] for i in range(n + 1))

    nearest_smaller = [n + 1] * (n + 1)

    for i in reversed(range(n)):
        j = i + 1

        while j <= n and prefix[i] <= prefix[j]:
            j = nearest_smaller[j]

        nearest_smaller[i] = j

    return sum(
        second_prefix[nearest_smaller[i]]
        - second_prefix[i + 1]
        - prefix[i] * (nearest_smaller[i] - i - 1)
        for i in range(n)
    )


if __name__ == "__main__":
    n_cases = int(input())

    for case in range(1, n_cases + 1):
        n = int(input())
        array = list(map(int, input().split()))
        print(f"Case #{case}:", subarrays(array, n))
