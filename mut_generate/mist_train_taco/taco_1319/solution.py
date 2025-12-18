"""
QUESTION:
To make one bouquet we need K adjacent flowers from the garden. Here the garden consists of N different flowers, the ith flower will bloom in the bloomDay[i]. Each flower can be used inside only one bouquets. We have to find the minimum number of days need to wait to make M bouquets from the garden. If we cannot make m bouquets, then return -1.
The first line of input contains two integers M and K.
The second line contains N space-separated integers of bloomDay[i] array.
Example 1:
Input:
M = 2, K = 3
bloomDay = [5, 5, 5, 5, 10, 5, 5]
Output:
10
Explanation:
As we need 2 (M = 2) bouquets and each should have 3 flowers,
After day 5: [x, x, x, x, _, x, x], we can make one bouquet of
the first three flowers that bloomed, but cannot make another bouquet.
After day 10: [x, x, x, x, x, x, x], Now we can make two bouquets,
taking 3 adjacent flowers in one bouquet.
Example 2:
Input: 
M = 3, K = 2
bloomDay = [1, 10, 3, 10, 2]
Output: 
-1
Explanation:
As 3 bouquets each having 2 flowers are needed, that means we need 6 flowers. 
But there are only 5 flowers so it is impossible to get the needed bouquets
therefore -1 will be returned.
Your Task:
Complete the function int solve(), which takes integer M, K, and a list of N integers as input and returns the  minimum number of days needed to wait to be able to make M bouquets from the garden.
 
Expected Time Complexity: O(N.log(maxVal)), where maxVal = max(bloomDay)
Expected Auxiliary Space: O(1)
Constraints:
1 <= N <= 10^{5}
1 <= M <= 10^{5}
1 <= K <= N
1 <= bloomDay[i] <= 10^{9}
"""

def min_days_to_make_bouquets(M: int, K: int, bloomDay: list[int]) -> int:
    if len(bloomDay) < M * K:
        return -1
    
    l = min(bloomDay)
    r = max(bloomDay)
    ans = -1
    
    while l <= r:
        mid = (l + r) // 2
        count = 0
        bq = 0
        
        for day in bloomDay:
            if count < K and day > mid:
                count = 0
            if day <= mid:
                count += 1
            if count == K:
                bq += 1
                count = 0
        
        if bq >= M:
            ans = mid
            r = mid - 1
        else:
            l = mid + 1
    
    return ans