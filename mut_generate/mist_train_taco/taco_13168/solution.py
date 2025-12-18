"""
QUESTION:
A(X) for positive integer X is the sum of factorials of its digits. For example, A(154) = 1! + 5! + 4!= 145.
Given a number N, find the minimum number X such that A(X) = N. You have to return a list of digits (without leading zeros) which represent the number X.
Example 1:
Input: N = 40321
Output: 18
Explanation: A(18)=1!+ 8! =40321 
Note that A(80) and A(81) are also 
40321, But 18 is the smallest 
number.
Example 2:
Input: N = 5040
Output: 7
Explanation: A(7) = 7! = 5040.
Your Task:
You don't need to read or print anything. Your task is to complete the function FactDigit() which takes N as input parameter and returns a list of digits which represent the number X.
Expected Time Complexity: O(X) where X ≤ 10^{6}
Expected Space Complexity: O(X)
Constraints:
1 ≤ N ≤ 10^{9}
"""

def find_min_X_for_A(N):
    # Precompute factorials of digits 1 through 9
    factorials = [1]  # 0! = 1
    for i in range(1, 10):
        factorials.append(factorials[-1] * i)
    
    # Result list to store the digits of X
    result = []
    
    # Helper function to find the minimum X
    def find_min_X_util(N, digit):
        if digit == 0:
            return
        if N >= factorials[digit]:
            result.append(digit)
            N -= factorials[digit]
            if N >= factorials[digit]:
                pass
            else:
                digit -= 1
        else:
            digit -= 1
        find_min_X_util(N, digit)
    
    # Start the recursive search from the largest digit (9)
    find_min_X_util(N, 9)
    
    # Reverse the result list to get the correct order of digits
    result.reverse()
    
    return result