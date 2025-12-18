"""
QUESTION:
You are required to build some sheets of rectangular shape of Area A. To build a sheet of an  Area A of Dimensions L & B. You have two conditions:
1) L and B can not be in decimals.
2) When L and B are even, L must be Equal to B.
Calculate the number of possible choices to build a sheet of area A.
Example 1:
Input: A = 4
Output: 2
Explaination: The possible combinations are (1, 4) 
and (2, 2). Note that order does not matter. (1, 4) 
and (4, 1) are same.
Example 2:
Input: A = 7
Output: 1
Explaination: The only possible combination is (1, 7).
Your Task:
You do not need to read input or print anything. Your task is to complete the function rectangleCount() which takes A as input parameters and returns the number of possible combinations of (L, B).
Expected Time Complexity: O( sqrt(A) )
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ A ≤ 10^{5}
"""

import math

def rectangle_count(A: int) -> int:
    lim = int(math.sqrt(A))
    count = 0
    
    for i in range(1, lim + 1):
        if A % i == 0:
            t = A // i
            if i % 2 == 0 and t % 2 == 0:
                if i == t:
                    count += 1
            else:
                count += 1
    
    return count