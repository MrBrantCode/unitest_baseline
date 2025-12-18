"""
QUESTION:
Count the number of palindromic numbers less than N.
Example 1:
Input:
N = 12
Output:
10
Explanation:
There are 10 palindrome number less than 12.
1 2 3 4 5 6 7 8 9 11
Example 2:
Input:
N = 104
Output:
19
Explanation:
There are 19 palindrome number less than 104.
Your Task:  
You don't need to read input or print anything. Your task is to complete the function palindromicNumbers() which takes an integer N as input parameter and returns the count of the number of the palindromic numbers which are less than N.
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
Constraints:
1 <= N <= 10^{5}
"""

def count_palindromic_numbers(N: int) -> int:
    count = 0
    for i in range(1, N):
        i_str = str(i)
        if i_str == i_str[::-1]:
            count += 1
    return count