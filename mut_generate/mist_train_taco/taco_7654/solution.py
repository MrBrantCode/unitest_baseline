"""
QUESTION:
Given an array A[] of N integers, where A[i] denotes the height of i^{th} tree. 
Geek needs to cut down M meters of wood. He has a woodcutting machine that works as follows:  Set the blade at a height parameter H, and the machine cuts off all trees having a height greater than H. The trees having less than height H remains intact.
Since Geek is an environmentalist, he doesn't want to cut woods more than necessary, so he set the height H as high as possible.
Find the maximum height H of the blade that still allows to cutoff at least M meters of wood.
Example 1:
Input:
A[] = {20, 15, 10, 17}
M = 7
Output: 15
Explanation: 
Set the height parameter to 15, then Geek can chop:
  1.5 metres from first tree
  2. 0 metres from second tree
  3. 0 metres from third tree
  4. 2 metres from fourth tree
  So in total Geek chopped 5 + 2 = 7 metres of wood.
Example 2:
Input:
A[] = {4, 42, 40, 26, 46}
M = 20
Output: 36
 
Your Task:  
You don't need to read input or print anything. Your task is to complete the function maxHeight() which takes an array and an integer and returns an integer as output.
Expected Time Complexity: O(N *logN)
Expected Auxiliary Space: O(1)
 
Constraints:
1 <= N <= 10^{6}
1 <= A[i] <=10^{6}
1 <= B <=2 * 10^{6}
"""

from typing import List

def find_max_height(A: List[int], M: int) -> int:
    def check(mid: int, arr: List[int], M: int) -> bool:
        wood_cut = 0
        for ele in arr:
            wood_cut += max(0, ele - mid)
            if wood_cut >= M:
                return True
        return False

    mn, mx = 0, max(A)
    while mn <= mx:
        mid = (mn + mx) // 2
        if check(mid, A, M):
            mn = mid + 1
        else:
            mx = mid - 1
    return mx