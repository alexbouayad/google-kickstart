SPECIAL_CHARS = "#@*&"


def fix(password):
    new_chars = []

    if all(ord(x) not in range(ord("A"), ord("Z") + 1) for x in password):
        new_chars.append("A")

    if all(ord(x) not in range(ord("a"), ord("z") + 1) for x in password):
        new_chars.append("a")

    if all(ord(x) not in range(ord("0"), ord("9") + 1) for x in password):
        new_chars.append("1")

    if all(x not in SPECIAL_CHARS for x in password):
        new_chars.append("#")

    new_chars.append("A" * (7 - len(password) - len(new_chars)))
    return f'{password}{"".join(new_chars)}'


if __name__ == "__main__":
    n_cases = int(input())

    for case in range(1, n_cases + 1):
        _ = input()
        password = input()
        print(f"Case #{case}: {fix(password)}")
