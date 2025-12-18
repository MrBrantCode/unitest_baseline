"""
QUESTION:
Mr. Modulo comes up with another problem related to modulo and this time he is interested in finding all the possible pairs a and b in the array arr[] such that a % b = k where k is a given integer. The array given will have distinct elements.
You are required to print how many such pairs exist.
Example 1:
Input:
N=5, K=3
arr[] = {2, 3, 5, 4, 7}
Output: 4
Explanation:
The pairs are -: 
7 % 4 = 3
3 % 4 = 3
3 % 5 = 3
3 % 7 = 3
 
Example 2:
Input:
N=2, K=3
arr[] = {1, 2} 
Output: 0
 
Your Task:
Since, this is a function problem. You don't need to take any input, as it is already accomplished by the driver code. You just need to complete the function printPairs() that takes array arr, integer n and integer k as parameters and return the total number of such pairs in the array.
 
Expected Time Complexity:  O(N* sqrt(max)) where max is the maximum element in the array.
Expected Auxiliary Space: O(N).
 
Constraints:
1 ≤ N ≤ 10^{4}
"""

def count_modulo_pairs(arr, n, k):
    def divisors(val):
        ans = []
        for i in range(1, int(val ** 0.5) + 1):
            if val % i == 0:
                if val // i == i:
                    ans.append(i)
                else:
                    ans.append(i)
                    ans.append(val // i)
        return ans

    arr.sort()
    count = 0
    _set = set(arr)
    
    for i in range(n):
        val = arr[i]
        if k in _set and val > k:
            count += 1
        if val >= k:
            arr_divisors = divisors(val - k)
            for j in arr_divisors:
                if j in _set and val % j == k and (val != j):
                    count += 1
    
    return count