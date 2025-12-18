"""
QUESTION:
Given two integers A and B.Find out the number of steps required to repeatedly subtract the smaller of the two from the larger until one of them becomes 0.
Example 1:
Input:
A=5,B=13
Output:
6
Explanation:
The steps are as follows:
(5,13)->(5,8)->(5,3)->(2,3)->(2,1)->(1,1)->(1,0)
Thus, 6 steps are required.
Example 2:
Input:
A=5,B=15
Output:
3
Explanation:
The steps are as follows:
(5,15)->(5,10)->(5,5)->(5,0).
Thus, 3 steps are required.
Your Task:
You don't need to read input or print anything. Your task is to complete the function repeatedSubtraction() which takes two integers A and B as input parameters and returns the number of steps required to repeatedly subtract until one of the numbers becomes 0.
Expected Time Complexity:O(Log(max(A,B))
Expected Auxillary Space:O(1)
Constraints:
1<=A,B<=10^{9}
"""

def count_subtraction_steps(A: int, B: int) -> int:
    steps = 0
    while A != 0 and B != 0:
        if A > B:
            A = A - B
        else:
            B = B - A
        steps += 1
    return steps