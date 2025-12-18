"""
QUESTION:
Given two numbers, A and B. Find the number of common divisors of A and B. 
 
Example 1:
Ã¢â¬â¹Input : A = 2 and B = 4
Output : 2
Explanation:
There are only two common divisor of 2 and 4.
That is 1 and 2.
Ã¢â¬â¹Example 2:
Input : A = 3 and B = 5 
Output :  1
 
Your Task:
This is a function problem. The input is already taken care of by the driver code. You only need to complete the function common_divisor() that takes an integer A, another integer B, and return the number of the common divisor of A and B. The driver code takes care of the printing.
Expected Time Complexity: O(SQRT(min(A,B))).
Expected Auxiliary Space: O(1).
 
Constraints:
1 ≤ A, B ≤ 10^{7}
"""

def count_common_divisors(A: int, B: int) -> int:
    # Initialize the count of common divisors
    common_divisors_count = 0
    
    # Find the minimum of A and B to limit the loop
    min_value = min(A, B)
    
    # Iterate from 1 to the square root of the minimum value
    for i in range(1, int(min_value**0.5) + 1):
        if A % i == 0 and B % i == 0:
            # If i is a common divisor, count it
            common_divisors_count += 1
            # Also count the corresponding divisor if it's different
            if i != min_value // i and A % (min_value // i) == 0 and B % (min_value // i) == 0:
                common_divisors_count += 1
    
    return common_divisors_count