n_cases = int(input())


def is_palindrome(string):
    n = len(string)
    return all(string[i] == string[n - 1 - i] for i in range(n // 2))


def add_letters(substrings, letters):
    new_substrings = set()

    for string in substrings:
        for letter in letters:
            new_string = string + letter

            if len(new_string) <= 4:
                new_substrings.add(new_string)
                continue

            if len(new_string) == 5 and not is_palindrome(new_string):
                new_substrings.add(new_string)
                continue

            if not (
                is_palindrome(new_string) or is_palindrome(new_string[1:])
            ):
                new_substrings.add(new_string[1:])

    return new_substrings


for case in range(1, n_cases + 1):
    result = "POSSIBLE"
    n = int(input())
    string = input()
    substrings = {""}

    for letter in string:
        substrings = add_letters(substrings, "01" if letter == "?" else letter)

        if not substrings:
            result = "IMPOSSIBLE"
            break

    print(f"Case #{case}: {result}")
