"""
QUESTION:
Given three positive integers x, y and n, the task is to find count of all numbers from 1 to n that can be formed using x and y. A number can be formed using x and y if we can get it by adding any number of occurrences of x and/or y.
 
Example 1:
Input:
x = 2, y = 3, n = 10
Output:
9
Explanation:
We can form 9 out of 10 numbers using
2 and 3 and 10; 2 = 2, 3 = 3, 4 = 2+2,
5 = 2+3, 6 = 3+3 7 = 2+2+3, 8 = 3+3+2,
9 = 3+3+3 , 10 = 3+3+2+2.
Example 2:
Input:
x = 5, y = 7, n = 10
Output:
3
Explanation:
We can form 3 out of 10 numbers using
5 and 7 and 10; 5 = 5, 7 = 7, 5+5 = 10.
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function getCount() which takes 3 Integers x,y and n respctively as input and returns the answer.
 
Expected Time Complexity: O(n)
Expected Auxiliary Space: O(n)
 
Constraints:
1 <= x,y,n <= 10^{5}
"""

def count_numbers_formed(x: int, y: int, n: int) -> int:
    arr = [False] * (n + 1)
    
    if x <= n:
        arr[x] = True
    if y <= n:
        arr[y] = True
    
    result = 0
    for i in range(min(x, y), n + 1):
        if arr[i]:
            if i + x <= n:
                arr[i + x] = True
            if i + y <= n:
                arr[i + y] = True
            result += 1
    
    return result