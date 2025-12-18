"""
QUESTION:
Given a number N.Check if it is tidy or not.
A tidy number is a number whose digits are in non-decreasing order.
Example 1:
Input: 
1234
Output:
1
Explanation:
Since 1<2<3<4,therefore the number is tidy.
Example 2:
Input: 
1243
Output:
0
Explanation:
4>3, so the number is not tidy.
Your Task:
You don't need to read input or print anything.Your task is to complete the function isTidy() which takes an Integer N as input parameter and returns 1 if it is tidy.Otherwise, it returns 0.
Expected Time Complexity:O(LogN)
Expected Auxillary Space:O(1)
Constraints:
1<=N<=10^{9}
"""

def is_tidy(N: int) -> int:
    # Convert the number to a string to easily access its digits
    str_N = str(N)
    
    # Create a sorted version of the string representation of the number
    sorted_str_N = sorted(str_N)
    
    # Compare the original string with the sorted string
    if str_N == ''.join(sorted_str_N):
        return 1
    else:
        return 0