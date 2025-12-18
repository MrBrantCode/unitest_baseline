"""
QUESTION:
Given a number s(in string form). Find the Smallest number (Not leading Zeros) which can be obtained by rearranging the digits of given number.
 
Example 1:
Input: s = "846903"
Output: 304689
Explanation: 304689 is the smallest number
by rearranging the digits.
Example 2:
Input: s = "55010"
Output: 10055
Explanation: 10055 is the smallest number 
by rearranging the digts.
 
Your Task:
You don't need to read or print anything. Your task is to complete the function minimum_number() which takes the number as input parameter and returns the smallest number than can be formed without leading zeros by rearranging the digits of the number.
 
Expected Time Complexity: O(N * log(N)) where N is the number of digits of the given number
Expected Space Complexity: O(1)
 
Constraints:
1 <= N <= 10^{5}
"""

def find_smallest_number(s: str) -> str:
    # Convert the string to a list of characters (digits)
    digits = list(s)
    
    # Sort the list of digits in ascending order
    digits.sort()
    
    # Find the first non-zero digit and swap it with the first digit
    for i in range(len(digits)):
        if int(digits[i]) > 0:
            # Swap the first digit with the first non-zero digit
            digits[0], digits[i] = digits[i], digits[0]
            break
    
    # Join the list of digits back into a string
    smallest_number = ''.join(digits)
    
    return smallest_number