"""
QUESTION:
A Lucky number is a number which has only the digits 4 and 7. There's a special function F(n) for a positive integer n that returns all good digits of number n from the left to the right. For example, the output for number 147 is number 47. There are two numbers :
	An integer a 
	A Lucky number b.
Find the minimum number c (c > a) such that F(c) = b.
 
Example 1:
Input:
a = 1, b = 7
Output:
7
Explanation:
The minimum number x greater than 1 such that
F(x) = 7, is 7 and so it is the answer. 
Example 2:
Input:
a = 5, b = 4
Output:
14
Explanation:
The minimum number x greater than 5 such that
F(x) = 4, is 14 and so it is the answer.
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function findTheNum() which takes 2 Integera a, and b as input and returns the minimum number x greater than a such that F(x) = b.
 
Expected Time Complexity: O(b)
Expected Auxiliary Space: O(1)
 
Constraints:
1 <= a,b <= 10^{5}
"""

def find_min_number_with_good_digits(a: int, b: str) -> int:
    def check(t: int) -> int:
        d = 1
        res = 0
        while t > 0:
            temp = t % 10
            if temp == 4 or temp == 7:
                res += temp * d
                d *= 10
            t //= 10
        return res
    
    ans = a + 1
    while True:
        if str(check(ans)) == b:
            return ans
        ans += 1