"""
QUESTION:
Function: `maxDistSeating`

You are given a `m * n` matrix `seats` which symbolizes the seating arrangement in a theater. A seat is represented by a `'.'` character if it is available, and by a `'#'` character if it is already occupied. Your task is to determine the maximum number of audience members that can be seated in the theater while respecting their preferences, which is that they prefer to sit in a seat that is not directly adjacent to another occupied seat (in all eight directions). Audience members can only be placed in seats that are available.

Constraints: `seats` contains only characters `'.'` and `'#'`, `m == seats.length`, `n == seats[i].length`, `1 <= m <= 8`, and `1 <= n <= 8`.
"""

def maxDistToASeat(seats):
    def can_seat_here(i, j):
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
            x, y = i + dx, j + dy
            if 0 <= x < len(seats) and 0 <= y < len(seats[0]) and seats[x][y] == '#':
                return False
        return True

    def backtrack(i, count):
        if count > max_count[0]:
            max_count[0] = count
        for j in range(len(seats[0])):
            if seats[i][j] == '.' and can_seat_here(i, j):
                seats[i] = seats[i][:j] + '#' + seats[i][j + 1:]
                if i + 1 < len(seats):
                    backtrack(i + 1, count + 1)
                else:
                    backtrack(i, count + 1)
                seats[i] = seats[i][:j] + '.' + seats[i][j + 1:]

    max_count = [0]
    backtrack(0, 0)
    return max_count[0]