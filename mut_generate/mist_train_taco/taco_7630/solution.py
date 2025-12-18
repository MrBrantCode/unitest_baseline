"""
QUESTION:
Given N numbers in an array. Your task is to keep at-most K numbers at the top (According to their frequency).  We basically need to print top k numbers when input stream has included k distinct elements, else need to print all distinct elements sorted by frequency.
Example 1:
Input:
N=5, K=4
arr[] = {5, 2, 1, 3, 2} 
Output: 5 2 5 1 2 5 1 2 3 5 2 1 3 5 
Explanation:
Firstly their was 5 whose frequency
is max till now. so print 5.
Then 2 , which is smaller than 5 but
their frequency is same so print 2 5.
Then 1, which is smallet among all the
number arrived, so print 1 2 5.
Then 3 , so print 1 2 3 5
Then again 2, which has the highest
frequency among all number so 2 1 3 5.
Example 2:
Input:
N=5, K=4
arr[] = {5, 2, 1, 3, 4} 
Output: 5 2 5 1 2 5 1 2 3 5 1 2 3 4 
Explanation:
Firstly their was 5 whose frequency is
max till now. so print 5.
Then 2 , which is smaller than 5 but
their frequency is same so print 2 5.
Then 1, Which is smallest among all the
number arrived, so print 1 2 5.
Then 3 , so print 1 2 3 5.
Then 4, so 1 2 3 4 as K is 4 so print
at-most k elements.
 
Your Task:
Since, this is a function problem. You don't need to take any input, as it is already accomplished by the driver code. You just need to complete the function kTop() that takes array a, integer n and integer k as parameters and returns the array that contains our desired output.
 
Expected Time Complexity: O(N*K).
Expected Auxiliary Space: O(N).
 
Constraints:
1 ≤ N,K ≤ 10^{3}
"""

def top_k_frequent_elements(arr, n, k):
    top = [0 for _ in range(k + 1)]
    freq = {i: 0 for i in range(k + 1)}
    ans = []
    
    for m in range(n):
        if arr[m] in freq:
            freq[arr[m]] += 1
        else:
            freq[arr[m]] = 1
        
        top[k] = arr[m]
        i = top.index(arr[m])
        i -= 1
        
        while i >= 0:
            if freq[top[i]] < freq[top[i + 1]]:
                top[i], top[i + 1] = top[i + 1], top[i]
            elif freq[top[i]] == freq[top[i + 1]] and top[i] > top[i + 1]:
                top[i], top[i + 1] = top[i + 1], top[i]
            else:
                break
            i -= 1
        
        i = 0
        while i < k and top[i] != 0:
            ans.append(top[i])
            i += 1
    
    return ans