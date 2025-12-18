"""
QUESTION:
Given two integers a and b. Write a program to find the number of digits in the product of these two integers.
Example 1:
Input: a = 12, b = 4
Output: 2 
Explanation: 12*4 = 48
Hence its a 2 digit number.
Example 2:
Input: a = -24, b = 33
Output: 3
Explanation: -24*33 = -792
Hence its a 3 digit number.
Your Task:  
You dont need to read input or print anything. Complete the function countDigits() which takes a and b as input parameter and returns the number of digits in the product of the two numbers.
Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)
Constraints:
-10^{8}<= a,b <=10^{8}
"""

def count_digits_in_product(a: int, b: int) -> int:
    product = a * b
    product_abs = abs(product)
    return len(str(product_abs))