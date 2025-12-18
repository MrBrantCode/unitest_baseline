"""
QUESTION:
Given two positive numbers L and R (L < R), find out the smallest twins in the range [L , R].Two numbers are twins if they are prime numbers and difference between them is 2.
Example 1:
Input: L = 0, R = 5
Output: [3, 5]
Explanation: Difference between 3 and 5 is 2
and also these two are smallest prime in range.
So the answer is 3, 5. 
Example 2:
Input: L = 5, R = 10
Output: [5, 7]
Explanation: Difference between 5 and 7 is 2
and also these two are smallest prime in range.
So the answer is 5, 7. 
Your Task:  
You dont need to read input or print anything. Complete the function primeTwins() which takes L and R as input parameter and returns a pair if exist else returns -1.
Expected Time Complexity: O(nloglogn)
Expected Auxiliary Space: O(n)
Constraints:
0<= L <=500
2<= R <=1000
"""

def is_prime(N):
    if N == 0 or N == 1:
        return False
    for i in range(2, int(N ** 0.5) + 1):
        if N % i == 0:
            return False
    return True

def find_smallest_twins(L, R):
    for i in range(L, R + 1):
        if is_prime(i) and is_prime(i + 2):
            return [i, i + 2]
    return [-1]