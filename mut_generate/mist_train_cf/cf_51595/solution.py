"""
QUESTION:
Write a function `maxStudents(seats, distractions)` that takes a 2D array `seats` representing the seat distribution in a classroom and a 2D array `distractions` representing the position of distractions in the classroom, and returns the maximum number of students that can take the exam together without any cheating being possible.

`seats` is an `m * n` matrix where `seats[i][j]` is either `'.'` (representing a good seat) or `'#'` (representing a broken seat). `distractions` is a `p * 2` matrix where `distractions[i] = [x, y]` indicates that there is a distraction at the `x`th row and `y`th column.

A student cannot be placed in a seat that is adjacent (including diagonally) to a distraction. Students must be placed in seats in good condition. Students can see the answers of those sitting next to the left, right, upper left, and upper right, but they cannot see the answers of the student sitting directly in front or behind them.

Constraints:

- `seats` contains only characters `'.'` and `'#'`.
- `m == seats.length`
- `n == seats[i].length`
- `1 <= m <= 8`
- `1 <= n <= 8`
- `distractions[i].length == 2`
- `0 <= distractions.length <= m * n`
- `0 <= distractions[i][j] < m (or n)`
"""

def maxStudents(seats, distractions):
    m, n = len(seats), len(seats[0])
    valids = []
    for i in range(m):
        disturb = [0]*n
        for j in range(n):
            if seats[i][j] == "#": 
                disturb[j] = 1
            elif i-1 > -1 and j-1 > -1 and seats[i-1][j-1] == '.' and [i-1, j-1] in distractions:
                disturb[j] = 1
            elif i-1 > -1 and seats[i-1][j] == '.' and [i-1, j] in distractions:
                disturb[j] = 1
            elif i-1 > -1 and j+1 < n and seats[i-1][j+1] == '.' and [i-1, j+1] in distractions:
                disturb[j] = 1
            elif j-1 > -1 and seats[i][j-1] == '.' and [i, j-1] in distractions:
                disturb[j] = 1
        valids.append(int(''.join([str(c) for c in disturb]), 2))
        
    for i in range(len(distractions)):
        valids[distractions[i][0]] += pow(2, distractions[i][1])

    dp = [-1 << 40] * (1 << n)
    dp[0] = 0
    for valid in valids:
        for state in reversed(range(1 << n)):
            if (state & valid) == state:
                cnt = bin(state).count('1')
                dp[state] = max(dp[state], dp[state & (state << 1)] + cnt)
    return max(dp)