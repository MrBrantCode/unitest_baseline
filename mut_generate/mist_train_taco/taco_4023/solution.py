"""
QUESTION:
Given a set of positive integers, find all its subsets.
Example 1 :
Input : 
array = {1, 2, 3}
Output :
// this space denotes null element. 
1
1 2
1 2 3
1 3
2
2 3
3
Explanation: 
The following are the subsets 
of the array {1, 2, 3}.
Example 2 :
Input :
array = {1, 2}
Output :
1 
1 2
2
Explanation :
The following are the 
subsets of {1, 2}.
Your task :
You don't have to read input or print anything. Your task is to complete the function subsets() which takes the array of integers as input and returns the list of list containing the subsets of the given set of numbers in lexicographical order.
 
Expected Time Complexity : O(2^n)))
Expected Auxiliary Space : O(2^n*length of each subset)
 
Constraints :
1 <= n <= 20
1 <= arr[i] <=10
"""

def find_subsets(arr):
    def subs(A, l, res):
        if len(A) == 0:
            res.append(l)
            return
        l1 = l[:]
        l2 = l[:]
        l2.append(A[0])
        subs(A[1:], l1, res)
        subs(A[1:], l2, res)

    res = []
    subs(arr, [], res)
    res.sort()
    return res