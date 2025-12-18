"""
QUESTION:
Boom numbers are numbers consisting only of digits 2 and 3. Given an integer K, display the K-th Boom number.
Example 1:
Input:
K = 5
Output: 32
Explanation:
The Boom series is 2, 3, 22, 23, 32, 33, 222....
and, for K=5, answer = 32
 
Example 2:
Input:
K = 100
Output: 322323
Your Task:  
You don't need to read input or print anything. Your task is to complete the function BoomNumber() which takes an interger K as input parameter and returns the K^{th} boom number in the form of a string.
 
Expected Time Complexity: O( log(K) )
Expected Auxiliary Space: O( log(K) )
Constraints:
1 ≤ K ≤ 10^{12}
"""

def get_kth_boom_number(K: int) -> str:
    res = ''
    d = {0: '2', 1: '3'}
    n = K + 1
    while n != 1:
        res += d[n % 2]
        n = n // 2
    return res[::-1]