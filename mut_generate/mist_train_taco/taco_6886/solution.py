"""
QUESTION:
Geek is given 4 queries by the mentor and he has to tell worst case time complexity of the following algorithm
1 - BinarySearch
2 - Merge Sort
3 - Selection Sort
4 - Quick Sort
Example:
Input:
1
Output:
logn
Explanation:
Query 1 point to Binary Search which has logn in worst case time complexity.
Example 2:
Input:
3
Output:
n^2
Your Task:
You don't have to read input or print anything. Your task is to complete the function TImeComplexity() which takes the integer n denoting the query number and print the worst case time complexity.
Constraint:
1<=n<=4
"""

def get_time_complexity(n: int) -> str:
    if n == 1:
        return 'logn'
    elif n == 2:
        return 'nlogn'
    elif n == 3 or n == 4:
        return 'n^2'