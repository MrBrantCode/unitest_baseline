"""
QUESTION:
Given an array A, we may rotate it by a non-negative integer K so that the array becomes A[K], A[K+1], A{K+2], ... A[A.length - 1], A[0], A[1], ..., A[K-1].  Afterward, any entries that are less than or equal to their index are worth 1 point. 

For example, if we have [2, 4, 1, 3, 0], and we rotate by K = 2, it becomes [1, 3, 0, 2, 4].  This is worth 3 points because 1 > 0 [no points], 3 > 1 [no points], 0 <= 2 [one point], 2 <= 3 [one point], 4 <= 4 [one point].

Over all possible rotations, return the rotation index K that corresponds to the highest score we could receive.  If there are multiple answers, return the smallest such index K.


Example 1:
Input: [2, 3, 1, 4, 0]
Output: 3
Explanation:  
Scores for each K are listed below: 
K = 0,  A = [2,3,1,4,0],    score 2
K = 1,  A = [3,1,4,0,2],    score 3
K = 2,  A = [1,4,0,2,3],    score 3
K = 3,  A = [4,0,2,3,1],    score 4
K = 4,  A = [0,2,3,1,4],    score 3


So we should choose K = 3, which has the highest score.

 


Example 2:
Input: [1, 3, 0, 2, 4]
Output: 0
Explanation:  A will always have 3 points no matter how it shifts.
So we will choose the smallest K, which is 0.


Note:


       A will have length at most 20000.
       A[i] will be in the range [0, A.length].
"""

def find_best_rotation_index(A):
    def rotate_array(arr, k):
        """ Rotate array `arr` by `k` positions to the right. """
        n = len(arr)
        return arr[-k:] + arr[:-k]
    
    def calculate_score(arr):
        """ Calculate the score of the array based on the given rules. """
        score = 0
        for i, value in enumerate(arr):
            if value <= i:
                score += 1
        return score
    
    n = len(A)
    max_score = -1
    best_k = 0
    
    for k in range(n):
        rotated_A = rotate_array(A, k)
        current_score = calculate_score(rotated_A)
        
        if current_score > max_score:
            max_score = current_score
            best_k = k
        elif current_score == max_score and k < best_k:
            best_k = k
    
    return best_k