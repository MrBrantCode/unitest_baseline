"""
QUESTION:
Adobe is weak in the concepts of string. He is given a number N and has to find N terms of that series. The series is 1, 2, 5, 8,15. . . 
Example 1:
Input:
N = 8
Output:
1 2 5 8 15 28 51 94
Explanation:
For N = 8, series comes out to be:
1 2 5 8 15 28 51 94
Example 2:
Input:
N = 3
Output:
1 2 5 
Explanation:
For N = 3, series comes out to be:
1 2 5 
Your Task:  
You don't need to read input or print anything. Your task is to complete the function printSeries() which takes an integer N as input parameter and return the list of the first N term of the series.
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
Constraints:
1 <= N <= 50
"""

def generate_series(N):
    if N <= 0:
        return []
    
    a = 1
    b = 2
    c = 5
    series = []
    
    for _ in range(N):
        series.append(a)
        d = a + b + c
        a = b
        b = c
        c = d
    
    return series