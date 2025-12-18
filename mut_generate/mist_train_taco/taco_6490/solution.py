"""
QUESTION:
Given two numbers A and B count all the number between the given range whose second least significant digit in the binary representation of the number is 1.
 
Example 1:
Input:
A = 1
B = 4
Output:
2
Explanation:
In the given range 2 (10)
and 3 (11) are the numbers
whose second least 
significant digit in its
binary representation is 1.
Example 2:
Input:
A = 8
B = 10
Output:
1
Explanation:
In the given range 10 (1010)
is the number whose second
least significant digit in its
binary representation is 1
Your Task:
You don't need to read input or print anything. Your task is to complete the function find() which takes integers A, B as input parameters and returns the count of all the numbers between the given range whose second least significant digit in the binary representation of the number is 1.
 
Expected Time Complexity: O(1)
Expected Space Complexity: O(1)
 
Constraints:
1 <= A,B <= 10^{9}
"""

def count_numbers_with_second_lsb_one(A: int, B: int) -> int:
    ans = 0
    
    # Adjust A to the next number where the second LSB is 1
    if A % 4 == 1:
        A += 3
        ans += 2
    elif A % 4 == 2:
        A += 2
        ans += 2
    elif A % 4 == 3:
        A += 1
        ans += 1
    
    # Adjust B to the previous number where the second LSB is 1
    if B % 4 == 2:
        B -= 2
        ans += 1
    elif B % 4 == 3:
        B -= 3
        ans += 2
    
    # Calculate the count of numbers in the adjusted range
    ans += (B - A) // 4 * 2
    
    return ans