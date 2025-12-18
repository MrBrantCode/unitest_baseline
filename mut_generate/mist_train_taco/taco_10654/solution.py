"""
QUESTION:
Find an n × n matrix with different numbers from 1 to n^2, so the sum in each row, column and both main diagonals are odd.


-----Input-----

The only line contains odd integer n (1 ≤ n ≤ 49).


-----Output-----

Print n lines with n integers. All the integers should be different and from 1 to n^2. The sum in each row, column and both main diagonals should be odd.


-----Examples-----
Input
1

Output
1

Input
3

Output
2 1 4
3 5 7
6 9 8
"""

def generate_odd_sum_matrix(n):
    # Generate odd and even numbers within the range 1 to n^2
    o = [i for i in range(1, n ** 2 + 1, 2)]
    e = [i for i in range(2, n ** 2, 2)]
    
    # Initialize the n x n matrix with zeros
    x = [[0 for _ in range(n)] for _ in range(n)]
    
    # Fill the matrix with odd numbers in a specific pattern
    for i in range(n):
        y = n // 2
        if y - i >= 0:
            for j in range(y - i, y + i + 1):
                x[i][j] = o.pop()
        else:
            for j in range(y + i - n + 1, y - i + n):
                x[i][j] = o.pop()
    
    # Fill the remaining positions with even numbers
    for i in range(n):
        for j in range(n):
            if x[i][j] == 0:
                x[i][j] = e.pop()
    
    return x