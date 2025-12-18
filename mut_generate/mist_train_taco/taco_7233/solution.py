"""
QUESTION:
Given a number N. The task is to print Floyd's triangle with N lines.
Example 1:
Input:
N = 4
Output:
1
2 3
4 5 6
7 8 9 10
Explanation:
For N = 4 there are 4 rows in the output
and the number of elements increases 
with an increase in the row.
 
Example 1:
Input:
N = 5
Output:
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
Explanation:
For N = 5 there are 5 rows in the output
and the number of elements increases 
with an increase in the row.
Your Task:  
You don't need to read input. Your task is to complete the function printFloydTriangle() which takes an integer N as input parameter and prints the triangle.
Expected Time Complexity: O(N^2)
Expected Auxiliary Space: O(1)
Constraints:
1 <= N <= 100
"""

def generate_floyd_triangle(N):
    triangle = []
    c = 1
    for i in range(1, N + 1):
        row = []
        for j in range(1, i + 1):
            row.append(c)
            c += 1
        triangle.append(row)
    return triangle