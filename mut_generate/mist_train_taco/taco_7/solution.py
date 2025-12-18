"""
QUESTION:
Arkady decides to observe a river for n consecutive days. The river's water level on each day is equal to some real value.

Arkady goes to the riverside each day and makes a mark on the side of the channel at the height of the water level, but if it coincides with a mark made before, no new mark is created. The water does not wash the marks away. Arkady writes down the number of marks strictly above the water level each day, on the i-th day this value is equal to mi.

Define di as the number of marks strictly under the water level on the i-th day. You are to find out the minimum possible sum of di over all days. There are no marks on the channel before the first day.

Input

The first line contains a single positive integer n (1 ≤ n ≤ 105) — the number of days.

The second line contains n space-separated integers m1, m2, ..., mn (0 ≤ mi < i) — the number of marks strictly above the water on each day.

Output

Output one single integer — the minimum possible sum of the number of marks strictly below the water level among all days.

Examples

Input

6
0 1 0 3 0 2


Output

6


Input

5
0 1 2 1 2


Output

1


Input

5
0 1 1 2 2


Output

0

Note

In the first example, the following figure shows an optimal case.

<image>

Note that on day 3, a new mark should be created because if not, there cannot be 3 marks above water on day 4. The total number of marks underwater is 0 + 0 + 2 + 0 + 3 + 1 = 6.

In the second example, the following figure shows an optimal case.

<image>
"""

def calculate_min_marks_below_water_level(n, marks_above):
    maxm = 0
    idx = 0
    ans = 0
    b = [0] * n
    
    # Find the maximum number of marks above water and its index
    for i in range(n):
        if marks_above[i] >= maxm:
            maxm = marks_above[i]
            idx = i
    
    # Set the number of marks on or after the day with the maximum marks above water
    for i in range(idx, n):
        b[i] = maxm + 1
    
    # Set the number of marks before the day with the maximum marks above water
    i = idx - 1
    while i >= 0:
        b[i] = max(marks_above[i] + 1, b[i + 1] - 1)
        i -= 1
    
    # Ensure the number of marks is non-decreasing
    for i in range(1, n):
        if b[i] < b[i - 1]:
            b[i] = b[i - 1]
        ans += b[i] - 1 - marks_above[i]
    
    return ans