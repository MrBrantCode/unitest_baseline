"""
QUESTION:
A special compression mechanism can arbitrarily delete 0 or more characters and replace them with the deleted character count.
Given two strings, S and T where S is a normal string and T is a compressed string, determine if the compressed string  T is valid for the plaintext string S. 
Note: If T consists of multiple integers adjacently, consider all of them at a single number. For example T="12B32", consider T as "12" + "B" + "32".  
Example 1:
Input:
S = "GEEKSFORGEEKS"
T = "G7G3S"
Output:
1
Explanation:
We can clearly see that T is a valid 
compressed string for S.
Example 2:
Input:
S = "DFS"
T = "D1D"
Output :
0
Explanation:
T is not a valid compressed string.
Your Task:  
You don't need to read input or print anything. Your task is to complete the function checkCompressed() which takes 2 strings S and T as input parameters and returns integer 1 if T is a valid compression of S and 0 otherwise.
Expected Time Complexity: O(|T|)
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ |S| ≤ 10^{6}
1 ≤ |T| ≤ 10^{6}
All characters are either capital or numeric.
"""

def check_compressed(S: str, T: str) -> int:
    c = 0
    j = 0
    k = 0
    for i in range(len(T)):
        if ord('0') <= ord(T[i]) <= ord('9'):
            c = c * 10 + int(T[i])
        else:
            j = j + c
            c = 0
            if j >= len(S):
                return 0
            if S[j] != T[i]:
                return 0
            j += 1
    j = j + c
    if j != len(S):
        return 0
    return 1