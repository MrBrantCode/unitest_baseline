"""
QUESTION:
You are given N ropes. A cut operation is performed on ropes such that all of them are reduced by the length of the smallest rope. Display the number of ropes left after every cut operation until the length of each rope is zero.
Example 1:
Input : arr[ ] = {5, 1, 1, 2, 3, 5} 
Output : 4 3 2 
Explanation: In the first operation, the 
minimum ropes are 1 So, we reduce length 1 
from all of them after reducing we left with 
4 ropes and we do the same for rest. 
 
Example 2:
Input : arr[ ] = {5, 1, 6, 9, 8, 11, 2, 
                               2, 6, 5} 
Output :  9 7 5 3 2 1
Your Task:
This is a function problem. The input is already taken care of by the driver code. You only need to complete the function RopeCutting() that takes an array (arr), sizeOfArray (n), and return the number of ropes that are left after each operation with space if no ropes left after one operation, in this case, return 0. The driver code takes care of the printing.
Expected Time Complexity: O(N*LOG(N)).
Expected Auxiliary Space: O(1).
 
Constraints:
1 ≤ N ≤ 10^{5}
"""

def rope_cutting(arr, n):
    if n == 0:
        return [0]
    
    ropes = sorted(arr)
    result = []
    cutting_length = ropes[0]
    
    for i in range(1, n):
        if ropes[i] - cutting_length > 0:
            result.append(n - i)
            cutting_length = ropes[i]
    
    if not result:
        return [0]
    
    return result