"""
QUESTION:
As we mentioned earlier, bitwise operations can be used to find number of subsets. Here, we will use that.
Given an array arr of N elements. The task is to count all the subsets whose sum is even.
Example:
Input:N = 3
arr[] = 1 2 3
Output:3
Explanation: Three subsets are there whose sum of elements is even. Subsets are (3, 2, 1), (1, 3), (2).
 
Your Task:
Your task is to complete the function countSumSubsets() which counts all the subsets in which sum of all the elements is even. Print the count of subsets whose sum of all elements is even.
Constraints:
1 <= N <= 10
1 <= arr[i] <= 10
"""

def count_even_sum_subsets(arr, N):
    def subs(idx, tmp, lst):
        if idx >= N:
            if sum(tmp) % 2 == 0:
                lst.append(tmp[:])
            return
        tmp.append(arr[idx])
        subs(idx + 1, tmp, lst)
        tmp.pop()
        subs(idx + 1, tmp, lst)

    lst = []
    subs(0, [], lst)
    return len(lst)