"""
QUESTION:
The task is to find the second smallest number with a given sum of digits as S and the number of digits as D.
Example 1:
Input:
S = 9 
D = 2
Output:
27
Explanation:
18 is the smallest number possible with sum = 9
and total digits = 2, Whereas the second
smallest is 27.
Example 2:
Input:
S = 16
D = 3
Output:
178
Explanation:
169 is the smallest number possible with sum is
16 and total digits = 3, Whereas the second
smallest is 178.
Your Task:
You don't need to read input or print anything. Your task is to complete the function secondSmallest() which takes the two integers S and D respectively and returns a string which is the second smallest number if possible, else return "-1".
Expected Time Complexity: O(D)
Expected Space Complexity: O(1)
Constraints:
1 ≤ S ≤ 10^{5}
1 ≤ D ≤ 10^{5}
"""

def second_smallest(S: int, D: int) -> str:
    if S <= 9 and D == 1:
        return str(S)
    if S >= 9 * D:
        return "-1"
    
    ret = []
    while S:
        if S >= 9:
            ret.append(9)
            S -= 9
        else:
            ret.append(S)
            S = 0
    
    if len(ret) < D:
        ret[-1] -= 1
        while len(ret) < D:
            ret.append(0)
        ret[-1] += 1
    
    for i in range(D):
        if ret[i] != 9:
            if i >= 1:
                ret[i] += 1
                ret[i - 1] -= 1
            else:
                ret[i] -= 1
                ret[i + 1] += 1
            break
    
    return ''.join(map(str, ret[::-1]))