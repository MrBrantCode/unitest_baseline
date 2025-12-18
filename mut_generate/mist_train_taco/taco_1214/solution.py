"""
QUESTION:
Given a number n, count the total number of digits required to write all numbers from 1 to n.
Example 1:
Input: n = 13
Output: 17 
Explanation: There are total 17 
digits required to write all 
numbers from 1 to 13.
Example 2:
Input: n = 4
Output: 4
Explanation: There are total 4 
digits required to write all
numbers from 1 to 4.
Your Task:  
You dont need to read input or print anything. Complete the function totalDigits() which takes n as input parameter and returns the total number of digits required to write all numbers from 1 to n.
Expected Time Complexity: O(logn)
Expected Auxiliary Space: O(1)
Constraints:
1<= n <=100000
"""

def count_total_digits(n: int) -> int:
    if n < 10:
        return n
    else:
        total_digits = 9
        for i in range(10, n + 1):
            total_digits += len(str(i))
        return total_digits