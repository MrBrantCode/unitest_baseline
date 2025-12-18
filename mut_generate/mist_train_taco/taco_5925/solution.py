"""
QUESTION:
Given a number N in the form of string, the task is to check if the number is divisible by 5. 
 
Example 1:
Input:
N = "5"
Output:
1
Explanation:
5 is divisible by 5.
 
Example 2:
Input:
N = "1000001"
Output:
0
Explanation:
1000001 is not divisible 
by 5.
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function divisibleBy5() which takes the string N and returns 1 if N is divisible by 5, else returns 0.
 
Expected Time Complexity: O(|N|)
Expected Auxiliary Space: O(1)
Constraints:
1<= N <=10^{5}
"""

def is_divisible_by_5(N: str) -> int:
    n = int(N)
    k = n % 10
    if k == 0 or k == 5:
        return 1
    else:
        return 0