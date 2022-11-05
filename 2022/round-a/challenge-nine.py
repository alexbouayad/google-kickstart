n_cases = int(input())

for case in range(1, n_cases + 1):
    digits = list(input())
    n_digits = len(digits)
    digits.append("b")
    new_digit = str((-sum(map(int, digits[:-1]))) % 9)
    start = 0
    prefix = []

    if new_digit == "0":
        prefix.append(digits[0])
        start = 1

    for i in range(start, n_digits + 1):
        if new_digit < digits[i]:
            prefix.append(new_digit)
            break

        prefix.append(digits[i])

    result = "".join(prefix + digits[i:-1])
    print(f"Case #{case}: {result}")
