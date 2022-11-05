from sys import setrecursionlimit

DIRECTIONS = "NWSE"
DELTAS = [(-1, 0), (0, -1), (1, 0), (0, 1)]


def path(n_rows, n_cols, matrix):
    moves = []

    def visit(i, j, prev):
        matrix[i][j] = "@"

        for k in range(1, 4):
            move_next = (prev + k) % 4
            i_delta, j_delta = DELTAS[move_next]
            i_next, j_next = i + i_delta, j + j_delta

            if (
                0 <= i_next < n_rows
                and 0 <= j_next < n_cols
                and matrix[i_next][j_next] == "*"
            ):
                moves.append(move_next)
                visit(i_next, j_next, (move_next + 2) % 4)
                moves.append((move_next + 2) % 4)

            else:
                moves.append((move_next + 1) % 4)

    visit(0, 0, 0)
    moves.append(1)
    moves = "".join([DIRECTIONS[idx] for idx in moves])
    return "IMPOSSIBLE" if any("*" in row for row in matrix) else moves


if __name__ == "__main__":
    n_cases = int(input())
    setrecursionlimit(1_000_000)

    for case in range(1, n_cases + 1):
        n_rows, n_cols = map(int, input().split())
        matrix = [list(input()) for _ in range(n_rows)]
        n_empty = sum(cell == "*" for row in matrix for cell in row)
        print(f"Case #{case}: {path(n_rows, n_cols, matrix)}")
