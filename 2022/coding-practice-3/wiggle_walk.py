from collections import defaultdict


class Graph:
    def __init__(self):
        self._dict = {}

    def __getitem__(self, key):
        x, y = key

        if key not in self._dict:
            self._dict[x, y] = {
                "N": (x - 1, y),
                "S": (x + 1, y),
                "E": (x, y + 1),
                "W": (x, y - 1),
                "#": (x, y)
            }

        return self._dict[key]


t = int(input())

for case_id in range(1, t + 1):
    *_, x, y = map(int, input().split())
    instructions = f"#{input()}"
    graph = Graph()

    for direction in instructions:
        x, y = graph[x, y][direction]

        north = graph[x, y]["N"]
        south = graph[x, y]["S"]
        east = graph[x, y]["E"]
        west = graph[x, y]["W"]

        graph[north]["S"] = south
        graph[south]["N"] = north
        graph[east]["W"] = west
        graph[west]["E"] = east

    print(f"Case #{case_id}: {x} {y}")
