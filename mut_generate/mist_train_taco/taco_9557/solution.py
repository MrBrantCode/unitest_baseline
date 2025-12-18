"""
QUESTION:
This task will exclusively concentrate only on the arrays where all elements equal 1 and/or 2.

Array a is k-period if its length is divisible by k and there is such array b of length k, that a is represented by array b written exactly $\frac{n}{k}$ times consecutively. In other words, array a is k-periodic, if it has period of length k.

For example, any array is n-periodic, where n is the array length. Array [2, 1, 2, 1, 2, 1] is at the same time 2-periodic and 6-periodic and array [1, 2, 1, 1, 2, 1, 1, 2, 1] is at the same time 3-periodic and 9-periodic.

For the given array a, consisting only of numbers one and two, find the minimum number of elements to change to make the array k-periodic. If the array already is k-periodic, then the required value equals 0.


-----Input-----

The first line of the input contains a pair of integers n, k (1 ≤ k ≤ n ≤ 100), where n is the length of the array and the value n is divisible by k. The second line contains the sequence of elements of the given array a_1, a_2, ..., a_{n} (1 ≤ a_{i} ≤ 2), a_{i} is the i-th element of the array.


-----Output-----

Print the minimum number of array elements we need to change to make the array k-periodic. If the array already is k-periodic, then print 0.


-----Examples-----
Input
6 2
2 1 2 2 2 1

Output
1

Input
8 4
1 1 2 1 1 1 2 1

Output
0

Input
9 3
2 1 1 1 2 1 1 1 2

Output
3



-----Note-----

In the first sample it is enough to change the fourth element from 2 to 1, then the array changes to [2, 1, 2, 1, 2, 1].

In the second sample, the given array already is 4-periodic.

In the third sample it is enough to replace each occurrence of number two by number one. In this case the array will look as [1, 1, 1, 1, 1, 1, 1, 1, 1] — this array is simultaneously 1-, 3- and 9-periodic.
"""

def min_changes_for_k_periodic(n, k, array):
    # Initialize a list to count occurrences of 1 in each period segment
    l = [0] * k
    
    # Count the number of 1s in each segment of length k
    for i in range(k):
        l[i] = array[i::k].count(1)
    
    # Calculate the number of changes needed
    ans = 0
    n //= k  # Number of segments
    for x in l:
        ans += min(x, n - x)
    
    return ans