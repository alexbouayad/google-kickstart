def curling(red_stones, yellow_stones, r_stone, r_house):
    red_squared_distances = [x**2 + y**2 for x, y in red_stones]
    yellow_squared_distances = [x**2 + y**2 for x, y in yellow_stones]

    return sum(
        d <= (r_house + r_stone) ** 2
        and ((not yellow_stones or d <= min(yellow_squared_distances)))
        for d in red_squared_distances
    ), sum(
        d <= (r_house + r_stone) ** 2
        and ((not red_stones or d <= min(red_squared_distances)))
        for d in yellow_squared_distances
    )


if __name__ == "__main__":
    n_cases = int(input())

    for case in range(1, n_cases + 1):
        r_stone, r_house = map(int, input().split())
        red_stones = [
            tuple(map(int, input().split())) for _ in range(int(input()))
        ]
        yellow_stones = [
            tuple(map(int, input().split())) for _ in range(int(input()))
        ]
        print(
            f"Case #{case}:",
            *curling(red_stones, yellow_stones, r_stone, r_house),
        )
