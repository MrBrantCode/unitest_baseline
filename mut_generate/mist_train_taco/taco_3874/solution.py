"""
QUESTION:
Find all valid combinations of K numbers that sum upto to N such that the following conditions are true:
	Only number 1 through 9 are used.
	Each number is used atmost once.
Return the list of all possible valid combinations.
Note: The list must not contain the same combination twice, and the combinations returned in any order.
 
Example 1:
Input:
K = 3
N = 7
Output: { {1, 2, 4} }
Explanation: 
1+ 2+ 4 = 7
There are no other valid combinations.
 
Example 2:
Input:
K = 3
N = 9
Output: { {1, 2, 6}, {1, 3, 5}, {2, 3, 4} }
Explanation: 
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
There are no other valid combinations.
 
Example 3:
Input:
K = 4
N = 3
Output: { { } }
Explanation: There are no valid combinations.
Using 4 different numbers in the range {1, 9}, the smallest sum we can get is 1 + 2 + 3 + 4 = 10 and since 10 > 3, there are no valid combinations.
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function combinationSum() which takes the integers K and N as parameters and returns a list of all possible valid combinations.
Expected Time Complexity: O(2^{K})
Expected Auxiliary Space: O(K)
Constraints:
1 ≤ K ≤ 9
^{1 }≤ N_{  }≤ 60
"""

def find_combinations(k, N):
    def combisum2(i, target, subs, arr, ans, n, num, k):
        if i == n:
            if target == 0 and num == k:
                ans.append(subs[:])
            return
        if target - arr[i] >= 0:
            subs.append(arr[i])
            num += 1
            combisum2(i + 1, target - arr[i], subs, arr, ans, n, num, k)
            num -= 1
            subs.pop()
        while i < n - 1 and arr[i] == arr[i + 1]:
            i += 1
        combisum2(i + 1, target, subs, arr, ans, n, num, k)

    candidates = list(range(1, 10))
    ans = []
    subs = []
    i = 0
    num = 0
    combisum2(i, N, subs, candidates, ans, 9, num, k)
    return ans