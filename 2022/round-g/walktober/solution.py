def walktober(scoreboard, n_participants, n_days, idx):
    n_participants = len(scoreboard)
    return sum(
        max(
            scoreboard[i][j] - scoreboard[idx - 1][j]
            for i in range(n_participants)
        )
        for j in range(n_days)
    )


if __name__ == "__main__":
    n_cases = int(input())

    for case in range(1, n_cases + 1):
        n_participants, n_days, idx = map(int, input().split())
        scoreboard = [
            list(map(int, input().split())) for _ in range(n_participants)
        ]
        print(
            f"Case #{case}: {walktober(scoreboard, n_participants, n_days, idx)}"
        )
