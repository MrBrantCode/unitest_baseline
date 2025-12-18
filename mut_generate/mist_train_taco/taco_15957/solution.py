"""
QUESTION:
Given a number N, check whether the number is Automorphic number or not.
A number is called Automorphic number if and only if its square ends in the same digits as the number itself. 
 
Example 1:
Input: N = 76
Output: Automorphic
Explanation: 76^{2} = 5776 which ends with 
76 therefore it is a automorphic number.
Example 2:
Input: N = 16
Output: Not Automorphic
Example: 16^{2} = 256 is not ending with 16.
 
Your Task:
You don't need to read or print anything. Your task is to complete the function is_AutomorphicNumber() which takes n as input parameter and returns "Automorphic" if it is Automorphic number otherwise returns "Not Automorphic"(Without quotes).
 
Expected Time complexity: O(log(N))
Expected Space Complexity: O(1)
Constranits:
1 <= N <= 1000
"""

def is_AutomorphicNumber(n: int) -> str:
    s = n ** 2
    q = str(s)
    n_str = str(n)
    if q.endswith(n_str):
        return 'Automorphic'
    return 'Not Automorphic'