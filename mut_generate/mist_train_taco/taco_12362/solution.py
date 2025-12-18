"""
QUESTION:
Link to Russian translation of the problem.

Kevin has an array A of N integers, but he doesn't like it - he only likes an array if all its neighboring elements are different (e.g. he likes the array [2,4,2,5,3,2,4], but not [1,2,3,3,4]).

Kevin can reverse any contiguous subarray of his array any number of times. For example, if he has the array [2,4,2,5,3,2,4] and reverses the subarray from 2^nd to 5^th element, he will obtain the array [2,3,5,2,4,2,4]. 

Now, Kevin wants to know the minimum number of reversals necessary to transform his array into an array he likes - if it's possible.

Input format:

The first line of the input will contain an integer N. The second line will contain N space-separated integers - the elements of A.

Output format:

If it's impossible to transform Kevin's array into an array he likes, print "-1" (without the quotes). Otherwise, print one number - the minimum number of reversals necessary.

Constraints:
1 ≤ N ≤ 10^5 
1 ≤ Ai ≤ 10^5
N ≤ 5 in test data worth 15% of all points
N ≤ 10^3 in test data worth 40% of all points

SAMPLE INPUT
7
1 3 2 2 4 4 4


SAMPLE OUTPUT
2

Explanation

First, Kevin reverses the subarray from the 3^rd to the 6^th element and gets the array [1,3,4,4,2,2,4]. Next, he reverses the elements from 4^th to 5^th and gets the array [1,3,4,2,4,2,4], which he likes. There's no way to create an array which Kevin likes using only one reversal.
"""

def min_reversals_to_like_array(N, A):
    if N == 1:
        return 0
    
    look = [0] * (max(A) + 1)
    look_count = [0] * (max(A) + 1)
    
    for i in range(N):
        look_count[A[i]] += 1
    
    for i in range(N - 1):
        if A[i] == A[i + 1]:
            look[A[i]] += 1
    
    mx = max(look)
    
    if max(look_count) > (N + 1) / 2:
        return -1
    else:
        return max(mx, (sum(look) + 1) // 2)