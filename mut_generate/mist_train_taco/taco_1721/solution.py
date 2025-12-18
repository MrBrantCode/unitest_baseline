"""
QUESTION:
Mahmoud has n line segments, the i-th of them has length a_{i}. Ehab challenged him to use exactly 3 line segments to form a non-degenerate triangle. Mahmoud doesn't accept challenges unless he is sure he can win, so he asked you to tell him if he should accept the challenge. Given the lengths of the line segments, check if he can choose exactly 3 of them to form a non-degenerate triangle.

Mahmoud should use exactly 3 line segments, he can't concatenate two line segments or change any length. A non-degenerate triangle is a triangle with positive area.


-----Input-----

The first line contains single integer n (3 ≤ n ≤ 10^5) — the number of line segments Mahmoud has.

The second line contains n integers a_1, a_2, ..., a_{n} (1 ≤ a_{i} ≤ 10^9) — the lengths of line segments Mahmoud has.


-----Output-----

In the only line print "YES" if he can choose exactly three line segments and form a non-degenerate triangle with them, and "NO" otherwise.


-----Examples-----
Input
5
1 5 3 2 4

Output
YES

Input
3
4 1 2

Output
NO



-----Note-----

For the first example, he can use line segments with lengths 2, 4 and 5 to form a non-degenerate triangle.
"""

def can_form_non_degenerate_triangle(n, lengths):
    # Sort the lengths of the line segments
    sorted_lengths = sorted(lengths)
    
    # Check if there exists a triplet (i, i+1, i+2) such that the sum of the first two is greater than the third
    for i in range(n - 2):
        if sorted_lengths[i] + sorted_lengths[i + 1] > sorted_lengths[i + 2]:
            return "YES"
    
    return "NO"