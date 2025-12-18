"""
QUESTION:
Write a function `calculate_gems(points, total_gems)` to find the number of gems of each type (A, B, and C) a player won, given the total points and the total number of gems. The points for each type of gem are 10 for A, 15 for B, and 20 for C. The function should return a list of three integers representing the number of gems of each type. If no solution is found, return None. The function should have a time complexity of O(N) or better.
"""

def calculate_gems(points, total_gems):
    for gems_C in range(0, total_gems+1):
        a = total_gems - gems_C
        b = points - 20 * gems_C
        if b % 5 == 0:
            gems_B = b // 15
            gems_A = a - gems_B
            if gems_A >= 0 and gems_B >= 0:
                return [gems_A, gems_B, gems_C]
    return None