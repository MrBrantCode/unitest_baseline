"""
QUESTION:
We have N sticks with negligible thickness.
The length of the i-th stick is A_i.
Snuke wants to select four different sticks from these sticks and form a rectangle (including a square), using the sticks as its sides.
Find the maximum possible area of the rectangle.

-----Constraints-----
 - 4 \leq N \leq 10^5
 - 1 \leq A_i \leq 10^9
 - A_i is an integer.

-----Input-----
Input is given from Standard Input in the following format:
N
A_1 A_2 ... A_N

-----Output-----
Print the maximum possible area of the rectangle.
If no rectangle can be formed, print 0.

-----Sample Input-----
6
3 1 2 4 2 1

-----Sample Output-----
2

1 \times 2 rectangle can be formed.
"""

def max_rectangle_area(sticks):
    # Sort the sticks in descending order
    sticks.sort(reverse=True)
    
    # Create a list of unique stick lengths in descending order
    unique_sticks = sorted(set(sticks), reverse=True)
    
    # Count the occurrences of each unique stick length
    counts = [0] * len(unique_sticks)
    j = 0
    counts[j] = 1
    for i in range(1, len(sticks)):
        if sticks[i - 1] == sticks[i]:
            counts[j] += 1
        else:
            j += 1
            counts[j] += 1
    
    # Find the maximum possible area of the rectangle
    max_area = 0
    for i in range(len(unique_sticks)):
        if counts[i] >= 4:
            max_area = unique_sticks[i] * unique_sticks[i]
            break
        elif counts[i] >= 2:
            for j in range(i + 1, len(unique_sticks)):
                if counts[j] >= 2:
                    max_area = unique_sticks[i] * unique_sticks[j]
                    break
            break
    
    return max_area