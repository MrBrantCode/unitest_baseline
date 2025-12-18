"""
QUESTION:
Given a number N, find the total sum of digits of all the numbers from 1 to N.
 
Example 1:
Input:
N = 5
Output:
15
Explanation:
Sum of digits of number from 1 to 5:
1 + 2 + 3 + 4 + 5 = 15
Example 2:
Input:
N = 12
Output
51
Explanation:
Sum of all digits from 1 to 12 is:
1+2+3+4+5+6+7+8+9+(1+0)+(1+1)+(1+2) = 51
Your Task:
You don't need to read input or print anything. Your task is to complete the function sumOfDigits() which takes an integer N as input parameter and returns the total sum of digits of all the numbers from 1 to N. 
 
Expected Time Complexity: O(D^{2}) (D is the number of digits in N)
Expected Space Complexity: O(D) (D is the number of digits in N)
 
Constraints:
1<= N <=1000000
"""

def sum_of_digits(N: int) -> int:
    total_sum = 0
    for i in range(1, N + 1):
        if i <= 9:
            total_sum += i
        else:
            x = 0
            while i > 0:
                last_digit = i % 10
                x += last_digit
                i //= 10
            total_sum += x
    return total_sum