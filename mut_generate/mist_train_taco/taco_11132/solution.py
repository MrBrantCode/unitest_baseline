"""
QUESTION:
Given the sum of length, breadth and height of a cuboid. The task is to find the maximum volume that can be achieved such that the sum of sides is S.
 
Example 1:
Input:
S = 8
Output:
18
Explanation:
All possible edge dimensions:
[1, 1, 6], volume = 6
[1, 2, 5], volume = 10
[1, 3, 4], volume = 12
[2, 2, 4], volume = 16
[2, 3, 3], volume = 18
So, Maximum possible Volume is 18.
Example 2:
Input:
S = 6
Output:
8
Explanation:
All possible edge dimensions:
[1, 1, 4], volume = 4
[1, 2, 3], volume = 6
[2, 2, 2], volume = 8
So, Maximum possible Volume is 8.
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function maximizeVolume() which takes an Integer S as input and returns the answer.
 
Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)
 
Constraints:
3 <= S <= 10^{6}
"""

def maximize_volume(S: int) -> int:
    l = S // 3
    S = S - l
    b = S // 2
    h = S - b
    return l * b * h