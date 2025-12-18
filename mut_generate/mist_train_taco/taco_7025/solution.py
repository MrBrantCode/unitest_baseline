"""
QUESTION:
You are given two arrays A and B each containing N numbers. You need to choose exactly one number from A and exactly one number from B such that the index of the two chosen numbers is not same and the sum of the 2 chosen values is minimum. Formally, if you chose ith element from A whose value is x and jth element from B whose value is y, you need to minimize the value of (x+y) such that i is not equal to j.
Your objective is to find this minimum value.
NOTE: If not possible print "-1" without quotes.
 
Example 1:
Input:
1
5
5 4 3 2 1
1 2 3 4 5
Output:
2
Explanation:
Minimum sum will be obtained by choosing
number at the last index of first array i.e.
5th element of the first array(1) and first
index of the second array ie first element
of second array (1).
Sum=1+1=2 as their indexes are different
but sum is minimum.
 
Your Task:  
You don't need to read input or print anything. Your task is to complete the function getMin() which takes the array A[], B[] and its size N as inputs and returns the required answer. If answer is not present, return -1.
Expected Time Complexity: O(N. Log(N))
Expected Auxiliary Space: O(N)
Constraints:
1 ≤ N ≤ 10^{5}
1 ≤ A[i], B[i] ≤ 10^{5}
"""

def get_min_sum(A, B, n):
    # Find the indices of the minimum values in A and B
    min_A_index = A.index(min(A))
    min_B_index = B.index(min(B))
    
    # If the indices are different, return the sum of the minimum values
    if min_A_index != min_B_index:
        return min(A) + min(B)
    
    # Initialize a list to store possible sums
    possible_sums = []
    
    # Iterate through all pairs of indices
    for i in range(n):
        for j in range(n):
            if i != j:
                possible_sums.append(A[i] + B[j])
    
    # If no valid sums were found, return -1
    if not possible_sums:
        return -1
    
    # Return the minimum sum from the possible sums
    return min(possible_sums)