DIRECTIONS = (
    "NWSE",
    [(-1, 0), (0, -1), (1, 0), (0, 1)],
)


def path(n_rows, n_cols, matrix):
    stack = [(0, 0, 0)]
    moves = []

    while stack:
        top = stack.pop()

        if type(top) is int:
            moves.append(top)
            continue

        i, j, prev = top

        if matrix[i][j] == "#":
            moves.append((prev - 1) % 4)
            continue

        matrix[i][j] = "#"
        stack.append(prev)

        for k in range(1, 4):
            move_next = (prev - k) % 4
            i_delta, j_delta = DIRECTIONS[1][move_next]
            i_next, j_next = i + i_delta, j + j_delta

            if 0 <= i_next < n_rows and 0 <= j_next < n_cols:
                stack.append((i_next, j_next, (move_next + 2) % 4))

            else:
                stack.append((move_next + 1) % 4)

        stack.append((prev + 2) % 4)

    moves = moves[1:-1]
    moves.append(1)
    moves = "".join(DIRECTIONS[0][idx] for idx in moves)
    return "IMPOSSIBLE" if any("*" in row for row in matrix) else moves


if __name__ == "__main__":
    n_cases = int(input())

    for case in range(1, n_cases + 1):
        n_rows, n_cols = map(int, input().split())
        matrix = [list(input()) for _ in range(n_rows)]
        print(f"Case #{case}: {path(n_rows, n_cols, matrix)}")
