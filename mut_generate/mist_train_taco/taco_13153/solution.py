"""
QUESTION:
Read problems statements in Mandarin Chinese . 

Given an array of n non-negative integers: A_{1}, A_{2}, …, A_{N}. Your mission is finding a pair of integers A_{u}, A_{v} (1 ≤  u < v ≤ N) such that (A_{u} and A_{v}) is as large as possible.
And is a bit-wise operation which is corresponding to & in C++ and Java.

------ Input ------ 

The first line of the input contains a single integer N. The ith line in the next N lines contains the A_{i}.

------ Output ------ 

Contains a single integer which is the largest value of A_{u} and A_{v} where 1 ≤  u < v ≤ N.

------ Constraints ------ 

50 points:
$2 ≤ N ≤ 5000$
$0 ≤ A_{i} ≤ 10^{9}$
50 points:
$2 ≤ N ≤ 3 × 10^{5}$
$0 ≤ A_{i} ≤ 10^{9}$

----- Sample Input 1 ------ 
4
2
4
8
10
----- Sample Output 1 ------ 
8
----- explanation 1 ------ 
2 and 4 = 0
2 and 8 = 0
2 and 10 = 2
4 and 8 = 0
4 and 10 = 0
8 and 10 = 8
"""

def find_max_bitwise_and_pair(A):
    # Sort the array in ascending order
    A.sort()
    
    # Initialize the maximum bitwise AND result to a very small number
    max_and = -1
    
    # Iterate over the array from the end to the beginning
    for i in range(len(A) - 1, 0, -1):
        # Calculate the bitwise AND of the current element and the previous element
        current_and = A[i] & A[i - 1]
        
        # Update the maximum bitwise AND if the current result is larger
        if current_and > max_and:
            max_and = current_and
    
    # Return the maximum bitwise AND found
    return max_and