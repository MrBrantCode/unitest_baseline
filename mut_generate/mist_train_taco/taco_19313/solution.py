"""
QUESTION:
Given an array Arr[] of N distinct integers and a range from L to R, the task is to count the number of triplets having a sum in the range [L, R].
Example 1:
Input:
N = 4
Arr = {8 , 3, 5, 2}
L = 7, R = 11
Output: 1
Explaination: There is only one triplet {2, 3, 5}
having sum 10 in range [7, 11].
Example 2:
Input:
N = 5
Arr = {5, 1, 4, 3, 2}
L = 2, R = 7
Output: 2
Explaination: There two triplets having 
sum in range [2, 7] are {1,4,2} and {1,3,2}.
Your Task:
You don't need to read input or print anything. Your task is to complete the function countTriplets() which takes the array Arr[] and its size N and L and R as input parameters and returns the count.
Expected Time Complexity: O(N^{2})
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ N ≤ 10^{3}
1 ≤ Arr[i] ≤ 10^{3}
1 ≤ L ≤ R ≤ 10^{9}
"""

def count_triplets_in_range(Arr, N, L, R):
    Arr.sort()
    a = 0
    b = 0
    
    # Count triplets with sum <= R
    for i in range(N - 2):
        j = i + 1
        k = N - 1
        while j < k:
            if Arr[i] + Arr[j] + Arr[k] <= R:
                a += k - j
                j += 1
            else:
                k -= 1
    
    # Count triplets with sum <= L-1
    for i in range(N - 2):
        j = i + 1
        k = N - 1
        while j < k:
            if Arr[i] + Arr[j] + Arr[k] <= L - 1:
                b += k - j
                j += 1
            else:
                k -= 1
    
    # The result is the difference between the two counts
    return a - b