"""
QUESTION:
You are given n numbers a_1, a_2, ..., a_{n}. You can perform at most k operations. For each operation you can multiply one of the numbers by x. We want to make [Image] as large as possible, where $1$ denotes the bitwise OR. 

Find the maximum possible value of [Image] after performing at most k operations optimally.


-----Input-----

The first line contains three integers n, k and x (1 ≤ n ≤ 200 000, 1 ≤ k ≤ 10, 2 ≤ x ≤ 8).

The second line contains n integers a_1, a_2, ..., a_{n} (0 ≤ a_{i} ≤ 10^9).


-----Output-----

Output the maximum value of a bitwise OR of sequence elements after performing operations.


-----Examples-----
Input
3 1 2
1 1 1

Output
3

Input
4 2 3
1 2 4 8

Output
79



-----Note-----

For the first sample, any possible choice of doing one operation will result the same three numbers 1, 1, 2 so the result is $1|1|2 = 3$. 

For the second sample if we multiply 8 by 3 two times we'll get 72. In this case the numbers will become 1, 2, 4, 72 so the OR value will be 79 and is the largest possible result.
"""

def maximize_bitwise_or(n, k, x, numbers):
    # Calculate the effective multiplier after k operations
    p = x ** k
    
    # Initialize arrays to store cumulative OR values
    x_cumulative_or = [0] * (n + 10)
    y_cumulative_or = [0] * (n + 10)
    
    # Calculate cumulative OR from left to right
    for i in range(n):
        x_cumulative_or[i + 1] = numbers[i] | x_cumulative_or[i]
    
    # Calculate cumulative OR from right to left
    for j in range(n - 1, -1, -1):
        y_cumulative_or[j] = numbers[j] | y_cumulative_or[j + 1]
    
    # Find the maximum bitwise OR after performing operations
    maxi = 0
    for i in range(n):
        current_or = x_cumulative_or[i] | (numbers[i] * p) | y_cumulative_or[i + 1]
        if current_or > maxi:
            maxi = current_or
    
    return maxi