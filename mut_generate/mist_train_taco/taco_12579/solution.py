"""
QUESTION:
My friend generated a series 1 4 8 9 12 17 25 28 .... . Each element of this series is known as "Dory". Your task is to find out whether a number n is Dory or not.
NOTE: If n is "Dory", then return 1 else return 0.
Example 1:
Input: n = 4
Output: 1 
Explanation: 4 is Dory because 
its present in the series.
Example 2:
Input: n = 7
Output: 0
Explanation: 7 is not Dory because
its not present in the series.
Your Task:  
You dont need to read input or print anything. Complete the function nisDoryOrNot() which takes n as input parameter and returns 1 If n is "Dory" else return 0.
Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)
Constraints:
1<= n <=10^{9}
"""

import math

def is_dory(n: int) -> int:
    x = 5 * n - 4
    y = 5 * n + 4
    x1 = int(math.sqrt(x))
    y1 = int(math.sqrt(y))
    if x1 ** 2 == x or y1 ** 2 == y:
        return 1
    return 0