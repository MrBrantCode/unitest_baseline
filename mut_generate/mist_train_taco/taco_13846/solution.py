"""
QUESTION:
Given an integer N the task is to find the largest number which is smaller or equal to it and has its digits in non-decreasing order.
 
Examples 1:
Input:
N = 200
Output:
199
Explanation:
If the given number 
is 200, the largest 
number which is smaller 
or equal to it having 
digits in non decreasing 
order is 199.
Example 2:
Input: 
N = 139
Output:
139
Explanation:
139 is itself in 
non-decresing order.
Your Task:
You don't need to read input or print anything. Your task is to complete the function find() which takes one integer value N, as input parameter and return the largest number which is smaller or equal to it and has its digits in non-decreasing order.
Expected Time Complexity: O(N)
Expected Space Complexity: O(1)
 
Constraints:
1<=N<=10^{5}
"""

def find_largest_non_decreasing_number(N: int) -> int:
    def is_non_decreasing_order(n: int) -> bool:
        n_str = str(n)
        for i in range(len(n_str) - 1):
            if int(n_str[i]) > int(n_str[i + 1]):
                return False
        return True
    
    while True:
        if is_non_decreasing_order(N):
            return N
        N -= 1