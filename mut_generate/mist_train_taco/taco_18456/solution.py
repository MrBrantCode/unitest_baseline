"""
QUESTION:
Given an array Arr of N integers.Calculate the sum of Bitwise ANDs(&) all the pairs formed by the given array.
Example 1:
Input:
N=3
Arr={5,10,15}
Output:
15
Explanation:
The bitwise Ands of all pairs are (5&10)=0
(5&15)=5 and (10&15)=10.Therefore,
total Sum=0+5+10=15.
Example 2:
Input:
N=4
Arr={10,20,30,40}
Output:
46
Explanation:
The sum of bitwise Ands 
of all pairs=0+10+8+20+0+8=46.
Your Task:
You don't need to read input or print anything.Your Task is to complete the function pairAndSum() which takes an Integer N and an array Arr as input parameters and returns the sum of bitwise Ands of all pairs.
Expected Time Complexity:O(N)
Expected Auxillary Space:O(1)
Constraints:
1<=N<=10^{5}
1<=Arr_{i}<=10^{8}
"""

def calculate_pair_and_sum(N, Arr):
    c = [0] * 32
    for i in range(N):
        for j in range(32):
            if Arr[i] & 1 << j:
                c[j] += 1
    ans = 0
    for i in range(32):
        ans += c[i] * (c[i] - 1) // 2 * (1 << i)
    return ans