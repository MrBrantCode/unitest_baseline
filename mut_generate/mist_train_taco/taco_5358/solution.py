"""
QUESTION:
You are given an array a consisting of n integers. We denote the subarray a[l..r] as the array [a_l, a_{l + 1}, ..., a_r] (1 ≤ l ≤ r ≤ n).

A subarray is considered good if every integer that occurs in this subarray occurs there exactly thrice. For example, the array [1, 2, 2, 2, 1, 1, 2, 2, 2] has three good subarrays:

  * a[1..6] = [1, 2, 2, 2, 1, 1]; 
  * a[2..4] = [2, 2, 2]; 
  * a[7..9] = [2, 2, 2]. 



Calculate the number of good subarrays of the given array a.

Input

The first line contains one integer n (1 ≤ n ≤ 5 ⋅ 10^5).

The second line contains n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ n).

Output

Print one integer — the number of good subarrays of the array a.

Examples

Input


9
1 2 2 2 1 1 2 2 2


Output


3


Input


10
1 2 3 4 1 2 3 1 2 3


Output


0


Input


12
1 2 3 4 3 4 2 1 3 4 2 1


Output


1
"""

import random

def count_good_subarrays(n, a):
    a.insert(0, 0)
    cnt = [0] * (n + 1)
    cnt2 = [0] * (n + 1)
    hashs = [0] * (n + 1)
    r1 = [None] * (n + 1)
    r2 = [None] * (n + 1)
    
    for i in range(1, n + 1):
        r1[i] = random.randint(1, 1000000000000)
        r2[i] = random.randint(1, 1000000000000)
    
    mpp = {0: 1}
    sum = 0
    l = 1
    ans = 0
    
    for i in range(1, n + 1):
        if cnt[a[i]] == 1:
            sum -= r1[a[i]]
        elif cnt[a[i]] == 2:
            sum -= r2[a[i]]
        
        cnt[a[i]] += 1
        
        if cnt[a[i]] == 1:
            sum += r1[a[i]]
        elif cnt[a[i]] == 2:
            sum += r2[a[i]]
        else:
            cnt[a[i]] = 0
        
        cnt2[a[i]] += 1
        
        while cnt2[a[i]] == 4:
            mpp[hashs[l - 1]] = mpp[hashs[l - 1]] - 1
            cnt2[a[l]] -= 1
            l += 1
        
        hashs[i] = sum
        tans = 0
        
        if sum in mpp:
            tans += mpp[sum]
            mpp[sum] = mpp[sum] + 1
        else:
            mpp[sum] = 1
        
        ans += tans
    
    return ans