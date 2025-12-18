"""
QUESTION:
Geek wants to buy chocolates. The shop only has two types of chocolates. One costs 3 rupees and the other cost 7 rupees. Geek has 100 rupees. Is it possible for him to save exactly N rupees after visiting the shop?
Example 1:
Input: N = 99
Output: 0
Explanation: Geek needs to save 99 rupees. 
That means he can only spend 1 rupee. But 
no chocolate is available for 1 rupee. Therefore 
there is no way for him to save N rupees. 
Example 2:
Input: N = 97
Output: 1
Explanation: Geek can buy one chocolate 
for 3 rupees and save 97 rupees.
Your Task:
You do not need to read input or print anything. Your task is to complete the function isPossible() which takes N as input parameter and returns 1 if Geek can save N rupees else returns 0.
Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)
Constraints:
0 ≤ N ≤ 100
"""

def can_save_exact_amount(N: int) -> int:
    for i in range(100):
        for j in range(100):
            if i * 3 + j * 7 == 100 - N:
                return 1
    return 0