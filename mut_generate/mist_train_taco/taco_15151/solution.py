"""
QUESTION:
Sandy is given an array of N integers which is a permutation of the first N natural numbers. He can swap any two elements of the array and can make at most K swaps. He needs to tell the largest permutation, in numerical order, could be made? You being sandy's friend help him in doing so.

Input Format:-
The first line of the input contains two integers, N and K, the size of the input array and the maximum swaps you can make, respectively. The second line of the input contains a permutation of the first N natural numbers.

Output Format:-
Print the lexicographically largest permutation you can make with at most K swaps.

Constraints:-
1 ≤ N ≤ 10^5
1 ≤ K ≤ 10^9

SAMPLE INPUT
5 1
4 2 3 5 1

SAMPLE OUTPUT
5 2 3 4 1

Explanation

Testcase 1:
You can swap any two numbers in [4,2,3,5,1] and see the largest permutation is [5,2,3,4,1]
Other Example:-
Input:-
3 1
2 1 3

Output:-
3 1 2

With 1 swap we can get [1,2,3], [3,1,2] and [2,3,1] out of these [3,1,2] is the largest permutation
"""

def largest_permutation(N, K, arr):
    if K >= N:
        # If K is greater than or equal to N, we can directly sort the array in descending order
        return sorted(arr, reverse=True)
    
    i = 0
    while i < K and N > 0:
        if i != arr.index(N):
            # Swap the current element with the largest remaining element
            arr[arr.index(N)], arr[i] = arr[i], arr[arr.index(N)]
        else:
            # If the current element is already the largest, we can use an extra swap
            K += 1
        i += 1
        N -= 1
    
    return arr