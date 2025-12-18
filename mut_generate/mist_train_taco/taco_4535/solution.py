"""
QUESTION:
Given a number, reverse it and add it to itself unless it becomes a palindrome or number of iterations becomes more than 5.
Example 1:
Input: n = 23
Output: 55 
Explanation: reverse(23) = 32,then 32+23
= 55 which is a palindrome. 
Example 2:
Input: n = 30
Output: 33
Explanation: reverse(30) = 3,then 3+30
= 33 which is palindrome. 
Your Task:  
You dont need to read input or print anything. Complete the function isSumPalindrome() which takes n as input parameter and returns that palindrome number if it becomes a palindrome else returns -1.
Expected Time Complexity: O(n*k),where k<=5.
Expected Auxiliary Space: O(1)
Constraints:
1<= n <=10^{4}
"""

def find_palindrome_or_return_minus_one(n: int) -> int:
    def is_palindrome(num: int) -> bool:
        return str(num) == str(num)[::-1]
    
    if is_palindrome(n):
        return n
    
    for _ in range(5):
        n += int(str(n)[::-1])
        if is_palindrome(n):
            return n
    
    return -1