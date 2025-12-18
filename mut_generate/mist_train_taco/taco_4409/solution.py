"""
QUESTION:
Given a non-negative number N in the form of string. The task is to apply at most one swap operation on the number N so that the result is just a previous possible number.
Note:  Leading zeros are not allowed.
 
Example 1:
Input :
S = "12435"
Output: 
12345
Explanation:
Although the number 12354 
will be the largest smaller 
number from 12435. But it is 
not possible to make it using 
only one swap. So swap 
4 and 3 and get 12345.
 
Example 2:
Input: 
S = " 12345"
Output: 
-1
Explanation:
Digits are in increasing order. 
So it is not possible to 
make a smaller number from it.
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function previousNumber() which takes the string S and returns the previous number of S. If no such number exists return -1;
 
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
 
Constraints:
2<=|Number length |<=10^{5}
"""

def previous_number(S: str) -> str:
    i = len(S) - 1
    f = 0
    while i > 0:
        if S[i] < S[i - 1]:
            f = 1
            j = i
            x = S[i - 1]
            first = i - 1
            while j < len(S):
                if x != S[j] and S[j] < S[i - 1]:
                    last = j
                    x = S[j]
                elif S[j] > S[i - 1]:
                    break
                j += 1
            if f == 1:
                break
        i -= 1
    if f == 0:
        return -1
    ans = ''
    for i in range(len(S)):
        if i == first:
            ans += S[last]
        elif i == last:
            ans += S[first]
        else:
            ans += S[i]
    if ans[0] == '0':
        return -1
    return ans