"""
QUESTION:
Ã¢â¬â¹Given a number x, your task is to find if this number is Deficient number or not. A number x is said to be Deficient Number if sum of all the divisors of the number denoted by divisorsSum(x) is less than twice the value of the number x. And the difference between these two values is called the deficiency.
Mathematically, if below condition holds the number is said to be Deficient:
divisorsSum(x) < 2*x
deficiency = (2*x) - divisorsSum(x)
Example 1:
Input: x = 21
Output: YES 
Explanation: Divisors are 1, 3, 7 and
21.Sum of divisors is 32. 
This sum is less than 2*21 or 42.
Example 2:
Input: x = 12
Output: NO
Explanation: Divisors are 1, 2, 3, 4,
6 and 12.Sum of divisors is 28.
This sum is not less than 2*12 or 24.
Your Task:  
You dont need to read input or print anything. Complete the function isDeficient() which takes x as input parameter and returns YES if the number is Deficient otherwise returns NO.
Expected Time Complexity: O(sqrt(n))
Expected Auxiliary Space: O(1)
Constraints:
1<= x <=10000000
"""

def is_deficient(x: int) -> str:
    c = 0
    for i in range(1, x + 1):
        if x % i == 0:
            c += i
    if c < 2 * x:
        return 'YES'
    else:
        return 'NO'