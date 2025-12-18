"""
QUESTION:
Given an array A of N integers. You have to find whether a combination of four elements in the array whose sum is equal to a given value X exists or not.
 
Example 1:
Input:
N = 6
A[] = {1, 5, 1, 0, 6, 0}
X = 7
Output:
1
Explantion:
1, 5, 1, 0 are the four elements which makes sum 7.
 
Your Task:  
You don't need to read input or print anything. Your task is to complete the function find4Numbers() which takes the array A[], its size N and an integer X as inputs and returns true if combination is found else false. Driver code will print 1 or 0 accordingly.
 
Expected Time Complexity: O(N^{3})
Expected Auxiliary Space: O(1)
 
Constraints:
4 <= N <= 100
1 <= A[i] <= 1000
"""

def find_four_elements_sum(A, X):
    n = len(A)
    if n < 4:
        return False
    
    A.sort()
    
    for i in range(n - 3):
        for j in range(i + 1, n - 2):
            left = j + 1
            right = n - 1
            while left < right:
                current_sum = A[i] + A[j] + A[left] + A[right]
                if current_sum == X:
                    return True
                elif current_sum < X:
                    left += 1
                else:
                    right -= 1
    return False