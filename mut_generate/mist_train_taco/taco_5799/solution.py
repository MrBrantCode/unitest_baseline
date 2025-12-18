"""
QUESTION:
Example

Input

10 3
3 7
8 9
2 5


Output

23
"""

def calculate_total_sum(n, m, ranges):
    # Initialize the array with 1s
    a = [1] * n
    
    # Apply each range to the array
    for c, d in ranges:
        for i in range(c, d):
            a[i] = 3
    
    # Calculate and return the total sum of the array
    return sum(a)