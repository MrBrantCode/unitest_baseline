"""
QUESTION:
Write a function `isEscapePossible` that takes in three parameters: `blocked`, `source`, and `target`. `blocked` is a list of lists of two integers, `source` and `target` are lists of two integers. The function should return `True` if it is possible to reach the `target` square from the `source` square by traversing one square in the north, east, south, or west direction without stepping outside the boundaries of a 1 million by 1 million grid or entering a blocked square. It is guaranteed that `source` and `target` are not blocked. The function should be efficient enough to handle up to 200 blocked squares and a grid of size 1 million by 1 million.
"""

def isEscapePossible(blocked, source, target):
    blocked = {tuple(p) for p in blocked}

    def bfs(source, target):
        bfs = [source]
        seen = {tuple(source)}
        for x0, y0 in bfs:
            for i, j in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                x, y = x0 + i, y0 + j
                if 0 <= x < 10**6 and 0 <= y < 10**6 and (x, y) not in blocked and (x, y) not in seen:
                    if [x, y] == target:
                        return True
                    bfs.append([x, y])
                    seen.add((x, y))
            if len(seen) > len(blocked):
                return True
        return False

    return bfs(source, target) and bfs(target, source)