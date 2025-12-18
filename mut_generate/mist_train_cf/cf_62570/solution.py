"""
QUESTION:
Implement a function `unhappy_matchings(n, preferences, pairs)` that takes three parameters: `n` (the total number of elements), `preferences` (a 2D list where `preferences[i]` represents the preference list of element `i` in decreasing order), and `pairs` (a list of pairs of matched elements). The function should return a tuple containing the number of unhappy elements and a list of pairs representing the unhappy matchings, sorted in a specific order and filtered to exclude elements paired with -1.
"""

def unhappy_matchings(n, preferences, pairs):
    order = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n-1):
            order[i][preferences[i][j]] = j

    match = [0]*n
    for x, y in pairs:
        match[x] = y
        match[y] = x

    unhappy = []
    for x in range(n):
        v = match[x]
        index = order[x][v]
        count = 0
        for i in range(index):
            u = preferences[x][i]
            v_ = match[u]
            if order[v_][x] < order[u][v_]:
                unhappy.append((x, u))
                count += 1
        if count == 0:
            unhappy.append((x, -1))

    unhappy.sort(key=lambda x: order[x[0]][match[x[0]]]-order[x[0]][x[1]], reverse=True)
    i = 0
    while i < len(unhappy) and unhappy[i][1] != -1:
        i += 1
    unhappy = unhappy[:i]

    return (len(unhappy), unhappy)