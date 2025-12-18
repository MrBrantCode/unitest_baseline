"""
QUESTION:
Ishaan is curious about numbers. He takes any 2 random numbers A and B. He wants to find out that whether A can be written as a sum of B distinct positive integers.Help him find out whether it is possible or not.
Example 1:
Input: A = 5, B = 2
Output: 1 
Explanation: 5 can be written as a 
sum of 2 numbers : 1+4 or 2+3.
Example 2:
Input: A = 6, B = 2
Output: 1
Explanation: 6 can be written as a 
sum of 2 numbers : 1+5 or 2+4.
Your Task:  
You dont need to read input or print anything. Complete the function kthDistinct() which takes n as input parameter and returns 1 if it is possible else return 0.
Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)
Constraints:
1<= A, B <=10^{6}
"""

def can_be_sum_of_distinct_positive_integers(A: int, B: int) -> int:
    if A >= B * (B + 1) // 2:
        return 1
    return 0