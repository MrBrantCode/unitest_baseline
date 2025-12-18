"""
QUESTION:
Given an integer N.Create a string using only lowercase characters from a to z that follows the given rules.
When N is even:
Use N/2 characters from the beginning of a-z and N/2 characters from the ending of a-z.
When N is greater than 26,continue repeating the instructions until length of string becomes N.
When N is odd:
Case 1: If the sum of digits of N is even, Select (N+1)/2 characters from the beginning of a-z and (N-1)/2 characters from the ending of a-z.
Case 2: If the sum of digits of N is odd, Select (N-1)/2 characters from the beginning of a-z and (N+1)/2 characters from the ending of a-z.
When N is greater than 26,continue repeating the instructions until length of string becomes N.
 
Example 1:
Input: 
N=21
Output: 
abcdefghijpqrstuvwxyz
Explanation:
Since 21 is odd and sum of digits
of 21 is also odd,we take (21-1)/2=10 
characters from the beginning and 
(21+1)/2=11 characters from the 
end of a-z.
Example 2: 
Input:
N=28 
Output: 
abcdefghijklmnopqrstuvwxyzaz
Explanation: 
Since 28>26, we keep repeating 
the process until length of string becomes 
28.
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function BalancedString() which takes the integer N as input parameter and returns the string created using given procedures.
 
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
 
Constraints:
1 <= N <= 10^{5}
"""

def generate_balanced_string(N: int) -> str:
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    output = ""
    
    # Calculate the number of full alphabets to include
    full_alphabets = N // 26
    output += alpha * full_alphabets
    
    # Calculate the remaining characters needed
    remaining = N % 26
    
    if remaining == 0:
        return output
    
    if remaining % 2 == 0:
        # If N is even
        half = remaining // 2
        output += alpha[:half] + alpha[-half:]
    else:
        # If N is odd
        sum_of_digits = sum(int(digit) for digit in str(N))
        if sum_of_digits % 2 == 0:
            # Sum of digits is even
            first_half = (remaining + 1) // 2
            second_half = (remaining - 1) // 2
            output += alpha[:first_half] + alpha[-second_half:]
        else:
            # Sum of digits is odd
            first_half = (remaining - 1) // 2
            second_half = (remaining + 1) // 2
            output += alpha[:first_half] + alpha[-second_half:]
    
    return output