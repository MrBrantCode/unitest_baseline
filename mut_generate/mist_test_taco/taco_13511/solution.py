"""
QUESTION:
Given a number S, check if it is divisible by 8. 
Example 1:
Input:
S=16
Output:
1
Explanation:
The given number is divisible by 8.
Example 2:
Input:
S=54141111648421214584416464555
Output:
-1
Explanation:
Given Number is not divisible by 8.
Your Task:
You don't need to read input or print anything.Your task is to complete the function DivisibleByEight() which takes a string S as input and returns 1 if the number is divisible by 8,else it returns -1.
Expected Time Complexity:O(1)
Expected Auxillary Space:O(1)
Constraints:
1 <= digits in S < 10^6
"""

def is_divisible_by_eight(S: str) -> int:
    def check(num: int) -> int:
        return 1 if num % 8 == 0 else -1
    
    if len(S) < 4:
        return check(int(S))
    else:
        num = S[len(S) - 3:]
        return check(int(num))