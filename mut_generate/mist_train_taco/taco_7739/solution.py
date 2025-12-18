"""
QUESTION:
Given a range of numbers starting with integer L and ending at R, the task is to count the numbers which have same first and last digits.
 
Example 1:
Input:
L = 7 
R = 68
Output:
9
Explanation:
Number with the same 
first and last digits 
in the given range is:
[7, 8, 9, 11, 22, 33, 
44 ,55, 66].
 
Example 2:
Input:
L = 5
R = 40
Output:
8
Explanation:
Number with the same
first and last digits
in the given range is:
[5, 6, 7, 8, 9, 11, 
22, 33, 44].
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function numbersInRange() which takes integers L and R and returns the count of numbers if L>R return 0.
 
Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)
 
Constraints:
1 <= L,R <= 10^{8}
"""

def count_numbers_with_same_first_and_last_digits(L, R):
    if L > R:
        return 0
    count = 0
    for i in range(L, R + 1):
        if str(i)[0] == str(i)[-1]:
            count += 1
    return count