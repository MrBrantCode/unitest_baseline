"""
QUESTION:
Given a palindromic number N in the form of string. The task is to find the smallest palindromic number greater than N using the same set of digits as in N.
Example 1:
Input: 
N = "35453"
Output: 
53435
Explanation: Next higher palindromic 
number is 53435.
Example 2:
Input: N = "33"
Output: -1
Explanation: Next higher palindromic number 
does not exist.
Your Task:  
You don't need to read input or print anything. Your task is to complete the function nextPalin() which takes the string N as input parameters and returns the answer, else if no such number exists returns "-1".
Expected Time Complexity: O(|N|log|N|)
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ |N| ≤ 10^{5}
"""

def next_palindromic_number(N: str) -> str:
    n = len(N) // 2
    ns = [int(N[n - 1])]
    i = n - 2
    
    while i >= 0:
        nn = int(N[i])
        mns = max(ns)
        
        if nn < mns:
            rn = min(nn + 1, mns)
            while rn not in ns:
                rn += 1
            if rn > mns:
                rn = mns
            ns.remove(rn)
            ns.append(nn)
            ns.sort()
            rs = str(rn) + ''.join([str(nm) for nm in ns])
            N = N[0:i] + rs + N[i + len(rs):len(N) - i - len(ns) - 1] + rs[::-1] + N[len(N) - i:]
            return N
        else:
            ns.append(nn)
            i -= 1
    
    return "-1"