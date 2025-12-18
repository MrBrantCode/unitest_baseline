"""
QUESTION:
Given two positive integers L and R, return count of numbers having exactly 3 divisors from L to R inclusive.
 
Example 1:
Input:
L = 1, R = 10
Output:
2
Explanation:
4 and 9 are two numbers between 1 and 10
and have exactly 3 divisors.
Example 2:
Input:
L = 2, R = 5
Output:
1
Explanation:
4 is the only number between 2 and 5
and have exactly 3 divisors.
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function count3DivNums() which takes 2 Integers L, and R as input and returns the count of numbers between L and R having exacly 3 divisors.
 
Expected Time Complexity: O(sqrt(R)*log(R))
Expected Auxiliary Space: O(sqrt(R))
 
Constraints:
1 <= L <= R <= 10^{9}
"""

def count_numbers_with_three_divisors(L, R):
    def is_prime(n):
        if n == 1:
            return False
        lim = int(n ** 0.5) + 1
        for i in range(2, lim):
            if n % i == 0:
                return False
        return True
    
    count = 0
    if L ** 0.5 == int(L ** 0.5):
        start = int(L ** 0.5)
    else:
        start = int(L ** 0.5) + 1
    end = int(R ** 0.5) + 1
    
    for i in range(start, end):
        if is_prime(i):
            count += 1
    
    return count