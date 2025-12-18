"""
QUESTION:
Three arrays of the same size are given. Find a triplet such that (maximum – minimum) in that triplet is the minimum of all the triplets. A triplet should be selected in a way such that it should have one number from each of the three given arrays. This triplet is the happiest among all the possible triplets. Print the triplet in decreasing order. If there are 2 or more smallest difference triplets, then the one with the smallest sum of its elements should be displayed.
Example 1:
Input:
N=3
a[] = { 5, 2, 8 }
b[] = { 10, 7, 12 }
c[] = { 9, 14, 6 }  
Output: 7 6 5
Explanation:
The triplet { 5,7,6 }  has difference
(maximum - minimum)= (7-5) =2 which is
minimum of all triplets.  
 
Example 2:
Input:
N=4
a[] = { 15, 12, 18, 9 }
b[] = { 10, 17, 13, 8 }
c[] = { 14, 16, 11, 5 }
Output: 11 10 9
Your Task:
Since, this is a function problem. You don't need to take any input, as it is already accomplished by the driver code. You just need to complete the function smallestDifferenceTriplet() that takes array arr1 , array arr2 ,array arr3 and integer n as parameters and returns the happiest triplet in an array.
 
Expected Time Complexity: O(NLogN).
Expected Auxiliary Space: O(1).
 
Constraints:
1 ≤ N ≤ 10^{5}
"""

def smallest_difference_triplet(a, b, c, n):
    # Sort the arrays
    a.sort()
    b.sort()
    c.sort()
    
    # Initialize indices for each array
    i = j = k = 0
    
    # Initialize the answer triplet and the minimum difference value
    ans = [a[0], b[0], c[0]]
    val = max(ans) - min(ans)
    
    # Iterate through the arrays
    while i < n and j < n and k < n:
        # Calculate the current triplet and its difference
        current_triplet = [a[i], b[j], c[k]]
        current_diff = max(current_triplet) - min(current_triplet)
        
        # Update the answer if the current triplet is better
        if current_diff < val or (current_diff == val and sum(ans) > sum(current_triplet)):
            ans = current_triplet
            val = current_diff
        
        # Move the index of the smallest element in the current triplet
        if a[i] <= b[j] and a[i] <= c[k]:
            i += 1
        elif b[j] <= a[i] and b[j] <= c[k]:
            j += 1
        else:
            k += 1
    
    # Sort the answer triplet in decreasing order
    ans.sort(reverse=True)
    
    return ans