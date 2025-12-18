"""
QUESTION:
Geek is playing a video game that contains N monsters having varying power denoted by power[i]. Geek will play total Q rounds and for each round, the power of Geek is Q[i]. He can kill all monsters having power <= Q[i].
All the monsters which were dead in the previous round will be reborn, such that for each round there will be N monsters.
Since Geek wants to win each round, he wants to count the number of monsters he can kill in each round and total sum of their powers. Can you help him?
Example 1:
Input:
N = 7
powers[] = {1, 2, 3, 4, 5, 6, 7}
Q[] = {3, 10, 2}
Output: 
{{3, 6}, {7, 28}, {2, 3}}
Explanation:
1. For round 1, Geek has power 3, hence, it can kill
the monsters with power 1, 2 and 3. Hence, count is 3 and
total sum = 1 + 2 + 3 = 6.
2. For round 2, Geek has power 10, hence, it can kill
all the monsters. Hence, count is 7 and
total sum = 1 + 2 + ...+ 7 = 28.
3. For round 3, Geek has power 2, hence, it can kill
the first two monsters. Hence, count is 2 and
total sum = 1 + 2 = 3.
Your Task:  
You don't need to read input or print anything. Your task is to complete the function win() which takes an array of size N and another array of size Q and return list of pairs as output.
Expected Time Complexity: O(N*logN)
Expected Auxiliary Space: O(N)
 
Constraints:
1 <= N <= 10^{4}
1 <= power[i] <= 10^{2}
1<= Q <=10^{4}
1 <= Q[i[ <= 10^{2}
"""

from typing import List, Tuple

def calculate_monster_kills(N: int, powers: List[int], Q: int, Q_powers: List[int]) -> List[Tuple[int, int]]:
    def binary_search(arr, ele):
        lo, hi = 0, len(arr) - 1
        ans = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if arr[mid] <= ele:
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return ans
    
    # Sort the powers array
    sorted_powers = sorted(powers)
    
    # Calculate the prefix sum of the sorted powers
    prefix_sum = sorted_powers[:]
    for i in range(1, N):
        prefix_sum[i] += prefix_sum[i - 1]
    
    result = []
    for power in Q_powers:
        idx = binary_search(sorted_powers, power)
        if idx == -1:
            result.append((0, 0))
        else:
            result.append((idx + 1, prefix_sum[idx]))
    
    return result