"""
QUESTION:
Write a function maxStudents(seats) that determines the maximum number of students that can be seated in a classroom such that no cheating is possible. The function takes a 2D array seats of size m * n, where seats[i][j] is '.' if the seat is in good condition and '#' if the seat is broken. The students can see the answers of their peers sitting to their left, right, upper left, and upper right, but they are unable to see the answers of the students sitting directly in front or behind them. The constraints are 1 <= m <= 8 and 1 <= n <= 8.
"""

def maxStudents(seats):
    m, n = len(seats), len(seats[0])
    full_bit_mask = (1 << n) - 1

    def countSetBits(n):
        count = 0
        while (n):
            count += n & 1
            n >>= 1
        return count

    valid_masks = [mask for mask in range(1 << n) if not (mask & (mask << 1)) and not (mask & (mask >> 1))]

    pre_row = [0 for _ in range(1 << n)]
    cur_row = [0 for _ in range(1 << n)]

    for i in range(m):
        availability_mask = int(''.join(('.' == cell) and '1' or '0' for cell in reversed(seats[i])), 2)
        for cur_mask in valid_masks:
            if cur_mask & availability_mask != cur_mask:
                continue
            max_students = -1
            for pre_mask in valid_masks:
                if pre_mask & (cur_mask << 1) or pre_mask & (cur_mask >> 1):
                    continue
                max_students = max(max_students, pre_row[pre_mask])
            if max_students != -1:
                cur_row[cur_mask] = max_students + countSetBits(cur_mask)

        pre_row, cur_row = cur_row, pre_row

    return max(pre_row)