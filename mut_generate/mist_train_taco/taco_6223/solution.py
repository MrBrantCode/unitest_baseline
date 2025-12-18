"""
QUESTION:
Given two numbers in the form of Strings. Find the count of carries in their addition.
 
Example 1:
Input:
N = "34", M = "25"
Output:
0
Explanation:
There are no carries when N and M
are added.
Example 2:
Input:
N = "4634", M = "1757"
Output:
2
Explanation:
There are 2 carries when N and M
are added.
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function getCarries() which takes two Strings N and M as input and returns an integer denoting the answer.
 
Expected Time Complexity: O(|N|)
Expected Auxiliary Space: O(|N|)
 
Constraints:
1 <= |N|,|M| <= 10^{5}
"""

def count_addition_carries(N: str, M: str) -> int:
    carries = 0
    no_of_carries = 0
    max_len = max(len(N), len(M))
    
    for i in range(max_len):
        digit_N = int(N[-i - 1]) if i < len(N) else 0
        digit_M = int(M[-i - 1]) if i < len(M) else 0
        
        summ = digit_N + digit_M + carries
        
        if summ >= 10:
            carries = 1
            no_of_carries += 1
        else:
            carries = 0
    
    return no_of_carries