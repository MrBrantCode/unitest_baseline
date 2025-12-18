"""
QUESTION:
Strong Numbers are the numbers whose sum of factorial of digits is equal to the original number. Given a number N, the task is to check if it is a Strong Number or not. Print 1 if the Number is Strong, else Print 0.
 
Example 1: 
Input:
N = 145
Output:
1
Explanation:
1! + 4! + 5! = 145 So, 145 is a Strong
Number and therefore the Output 1.
Example 2: 
Input:
N = 14
Output:
0
Explanation:
1! + 4! = 25 So, 14 isn't a Strong
Number and therefore the Output "NO".
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function isStrong() which takes an Integer N as input and returns the answer.
 
Expected Time Complexity: O(|N|)
Expected Auxiliary Space: O(1)
 
Constraints:
1 <= N <= 10^{8}
"""

def is_strong_number(N: int) -> int:
    def factorial(n: int) -> int:
        if n == 0 or n == 1:
            return 1
        return n * factorial(n - 1)
    
    sum_of_factorials = 0
    original_number = N
    
    while N != 0:
        digit = N % 10
        sum_of_factorials += factorial(digit)
        N //= 10
    
    if sum_of_factorials == original_number:
        return 1
    else:
        return 0