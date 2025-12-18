"""
QUESTION:
Petya has k matches, placed in n matchboxes lying in a line from left to right. We know that k is divisible by n. Petya wants all boxes to have the same number of matches inside. For that, he can move a match from its box to the adjacent one in one move. How many such moves does he need to achieve the desired configuration?


-----Input-----

The first line contains integer n (1 ≤ n ≤ 50000). The second line contains n non-negative numbers that do not exceed 10^9, the i-th written number is the number of matches in the i-th matchbox. It is guaranteed that the total number of matches is divisible by n.


-----Output-----

Print the total minimum number of moves.


-----Examples-----
Input
6
1 6 2 5 3 7

Output
12
"""

def calculate_minimum_moves(n, matches):
    total_matches = sum(matches)
    target_matches_per_box = total_matches // n
    moves = 0
    
    for i in range(n - 1):
        difference = target_matches_per_box - matches[i]
        matches[i] = target_matches_per_box
        matches[i + 1] -= difference
        moves += abs(difference)
    
    return moves