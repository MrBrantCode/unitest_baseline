"""
QUESTION:
Given a number N, write a program to check whether given number is Adam Number or not.
Adam number is a number when reversed, the square of the number and the square of the reversed number should be numbers which are reverse of each other.
 
Example 1: 
Input: 
N = 12
Output:
YES
Explanation:
12^{2} = 144 and 21^{2} = 441. 144 reversed 
gives 441, So, it's an Adam Number.
Example 1: 
Input: 
N = 14
Output:
NO
Explanation:
14^{2} = 196. 196 reversed gives 691,
which isn't equal to 41^{2} So,
it's not an Adam Number.
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function checkAdamOrNot() which takes an Integer N as input and returns the answer as "YES" if it is a Adam, number. Otherwise, returns "NO".
 
Expected Time Complexity: O(|N|)
Expected Auxiliary Space: O(1)
 
Constraints:
1 <= N <= 10^{4}
"""

def is_adam_number(N):
    # Reverse the number N
    dn = N
    rev = 0
    while dn != 0:
        rev = rev * 10 + dn % 10
        dn = dn // 10
    
    # Square of the original number and the reversed number
    sn = N * N
    srn = rev * rev
    
    # Reverse the square of the reversed number
    srev = 0
    dr = srn
    while dr != 0:
        srev = srev * 10 + dr % 10
        dr = dr // 10
    
    # Check if the reversed square of the reversed number is equal to the square of the original number
    if srev == sn:
        return 'YES'
    return 'NO'