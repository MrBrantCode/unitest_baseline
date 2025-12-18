"""
QUESTION:
Given n arrays of size m each. Find maximum sum obtained by selecting a number from each array such that the element selected from the i-th array is more than the element selected from (i-1)-th array. If maximum sum cannot be obtained then return 0.
Example 1:
Ã¢â¬â¹Input : arr[ ] = {{1,7,4,3}, {4,2,5,1}, {9,5,1,8}}
Output : 18
Explanation:
We can select 4 from the first array,
5 from second array and 9 from the third array.
Ã¢â¬â¹Example 2:
Input : arr[ ] = {{9,8,7}, {6,5,4}, {3,2,1}} 
Output :  0
Your Task:
This is a function problem. The input is already taken care of by the driver code. You only need to complete the function maximumSum() that takes number of row N, a number of Column M, 2-d array (arr), and return the maximum sum if cannot be obtained then return 0. The driver code takes care of the printing.
Expected Time Complexity: O(N*M).
Expected Auxiliary Space: O(1).
 
Constraints:
1 ≤ N, M ≤ 500
"""

def calculate_maximum_sum(arr, n, m):
    try:
        # Sort each array in descending order
        for i in range(n):
            arr[i].sort(reverse=True)
        
        # Ensure each element in the current array is less than the next array's first element
        for i in reversed(range(n - 1)):
            while arr[i][0] >= arr[i + 1][0]:
                arr[i].pop(0)
                if len(arr[i]) == 0:
                    break
        
        # Calculate the maximum sum
        ans = 0
        for i in range(n):
            if len(arr[i]) == 0:
                ans = 0
                break
            ans += arr[i][0]
        
        return ans
    except:
        return 0