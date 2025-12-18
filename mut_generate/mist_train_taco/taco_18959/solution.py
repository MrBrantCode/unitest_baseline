"""
QUESTION:
Mr. Modulo lives up to his name and is always busy taking modulo of numbers and making new problems.
Now he comes up with another problem. He has an array of integers with n elements and wants to find a pair of elements {arr[i], arr[j]} such that arr[i] ≥ arr[j] and arr[i] % arr[j] is maximum among all possible pairs where 1 ≤ i, j ≤ n.
Mr. Modulo needs some help to solve this problem. Help him to find this maximum value arr[i] % arr[j]. 
 
Example 1:
Input:
n=3
arr[] = {3, 4, 7} 
Output: 3
Explanation: There are 3 pairs which satisfies 
             arr[i] >= arr[j] are:-
             4, 3 => 4 % 3 = 1
             7, 3 => 7 % 3 = 1
             7, 4 => 7 % 4 = 3
             Hence maximum value among all is 3.
Example 2:
Input:
n=4
arr[] = {4, 4, 4, 4} 
Output: 0
Your Task:
Since, this is a function problem. You don't need to take any input, as it is already accomplished by the driver code. You just need to complete the function maxModValue() that takes array arr and n as parameters and return the required answer.
 
Expected Time Complexity: O(nLog(n) + Mlog(M)) n is total number of elements and M is maximum value of all the elements.
Expected Auxiliary Space: O(1).
 
Constraints:
1 ≤ n ≤ 10^{5}
1 ≤ arr[i] ≤ 10^{5}
"""

from bisect import bisect_left

def maxModValue(arr, n):
    arr.sort()
    ans = 0
    for i in range(n):
        for j in range(2 * arr[i], arr[i] + arr[n - 1], arr[i]):
            ind = bisect_left(arr, j) - 1
            ans = max(ans, arr[ind] % arr[i])
    return ans