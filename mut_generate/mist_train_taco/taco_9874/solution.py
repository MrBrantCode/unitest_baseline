"""
QUESTION:
Given two numbers you will have to check whether the first number is greater than or less than or equals to the second number.
Example 1:
Input:
A = 90
B = 5
Output:
90 is greater than 5.
Explanation:
Since A > B
So we print 90 is greater than 5.
Example 2:
Input:
A = 182
B = 234
Output:
182 is less than 234.
Explanation:
Since A < B
So we print 182 is less than 234.
Your Task:  
You don't need to read inputs. Your task is to complete the function relationalOperators() which takes two integers A and B and 
	If A > B then print "A is greater than B" without quotes
	If A < B then print "A is less than B" without quotes
	if A = B then print "A is equal to B" without quotes
Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)
Constraints:
1<= A,B <=10^{9}
"""

def compare_numbers(A: int, B: int) -> str:
    if A > B:
        return f"{A} is greater than {B}"
    elif A < B:
        return f"{A} is less than {B}"
    else:
        return f"{A} is equal to {B}"