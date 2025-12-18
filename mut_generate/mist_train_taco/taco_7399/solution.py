"""
QUESTION:
Given two numbers A and B, find K^{th} digit from right of A^{B}.
 
Example 1:
Input:
A = 3
B = 3
K = 1
Output:
7
Explanation:
3^{3 }= 27 and 1st
digit from right is 
7
Example 2:
Input:
A = 5
B = 2
K = 2
Output:
2
Explanation:
5^{2 }= 25 and second
digit from right is
2.
Your Task:
You don't need to read input or print anything. Your task is to complete the function kthDigit() which takes integers A, B, K as input parameters and returns K^{th }Digit of A^{B} from right side.
 
Expected Time Complexity: O(log A^{B})
Expected Space Complexity: O(1)
 
Constraints:
1 <= A,B <= 15
1 <=K<= digits in A^{B}
"""

def kth_digit_from_right(A: int, B: int, K: int) -> int:
    # Calculate A raised to the power of B
    val = A ** B
    
    # Convert the result to a string and reverse it
    val_str = str(val)[::-1]
    
    # Return the K-th digit from the right (1-based index)
    return int(val_str[K - 1])