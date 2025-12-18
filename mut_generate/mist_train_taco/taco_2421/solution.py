"""
QUESTION:
Given a number X and another number Y . There are a total  N cycles ,  and alternatively we perform operation on each number . In each cycle , we multiply the number by 2 . Starting with X .
Suppose after all the N cycles, the number X has become W and  number Y has become Z . Find the integer division of the maximum number among W and Z by the minimum number among W and Z .
 
Example 1:
Input: x = 1, y = 2, n = 1
Output: 2
Explanation:  the initial numbers are (X = 1,
Y = 2). There is only one turn. In this turn X 
is multiplied by 2. Hence, we get (X = 2, 
Y = 2) 
Therefore W = 2, and Z = 2. 
max (W , Z) / min (W , Z) =  2 / 2  = 1. 
Hence the first output is 1.
Example 2:
Input: x = 3, y = 2, n = 3
Output: 3
Explanation: the initial numbers are (X = 3,
Y = 2). There three turns. In the first cycle 
X is multiplied by 2.So, we get (X = 6, Y = 2).
In the second cycle Y (Y = 2) multiplies his 
number by 2. Hence, we get  ( X = 6,  Y = 4 ). 
In the third cycle  X ( X = 6) is multiplied by 
2. So, we get (X = 12, Y = 4) . As N = 3 , 
completed with 3 cyles, therefore W = 12 and 
Z = 4. max (W ,  Z) / min (W , Z) = 12 / 4 = 3. 
Hence the second output is 3. 
 
Your Task:
You don't need to read or print anyhting. Your task is to complete the function find_division() which takes X, Y and N as input parameter and returns the integer division of max(w, z) / min(w, z)
 
Expected Time Complexity: O(1)
Expected Space Complexity: O(1)
 
Constraints:
1 <= X, Y <= 10^{8}
1 <= N <= 10^{9}
"""

def find_division(x: int, y: int, n: int) -> int:
    if n % 2 == 0:
        return max(x, y) // min(x, y)
    else:
        x = x * 2
        return max(x, y) // min(x, y)