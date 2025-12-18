"""
QUESTION:
Given a string S created by a cypher algorithm. Find the original hexadecimal string.
The cypher algorithm: A hexadecimal string is XORed, N number of times, where N is the string length and every XOR operation is done after shifting the consecutive string to the right.
For example : String: "abcd".  
 
Example 1:
Input:
S = A1D0A1D
Output:
ABCD
Explanation:
Look at the matrix given in the problem statement.
Example 2:
Input:
S = 653CABEBD24
Output:
556F64
Explanation:
556F64
 556F64
  556F64
   556F64
    556F64
     556F64
653CABEBD24
Your Task:
You don't need to read input or print anything. Your task is to complete the function deCypher() which takes the string S as input parameter and returns the original hexadecimal string.
Note: Alphabets are in uppercase.
Expected Time Complexity: O(N)
Expected Space Complexity: O(N)
 
Constraints:
1<=N<=1001 & N%2=1
"""

def deCypher(S: str) -> str:
    plain = ''
    x = 0
    l = len(S)
    for i in range(l - 1, int(l / 2) - 1, -1):
        y = x ^ int(S[i], 16)
        x = x ^ y
        plain = hex(y)[-1] + plain
    return plain.upper()