"""
QUESTION:
You are given an array $a$ consisting of $n$ integers. Each $a_i$ is one of the six following numbers: $4, 8, 15, 16, 23, 42$.

Your task is to remove the minimum number of elements to make this array good.

An array of length $k$ is called good if $k$ is divisible by $6$ and it is possible to split it into $\frac{k}{6}$ subsequences $4, 8, 15, 16, 23, 42$.

Examples of good arrays:  $[4, 8, 15, 16, 23, 42]$ (the whole array is a required sequence);  $[4, 8, 4, 15, 16, 8, 23, 15, 16, 42, 23, 42]$ (the first sequence is formed from first, second, fourth, fifth, seventh and tenth elements and the second one is formed from remaining elements);  $[]$ (the empty array is good). 

Examples of bad arrays:   $[4, 8, 15, 16, 42, 23]$ (the order of elements should be exactly $4, 8, 15, 16, 23, 42$);  $[4, 8, 15, 16, 23, 42, 4]$ (the length of the array is not divisible by $6$);  $[4, 8, 15, 16, 23, 42, 4, 8, 15, 16, 23, 23]$ (the first sequence can be formed from first six elements but the remaining array cannot form the required sequence). 


-----Input-----

The first line of the input contains one integer $n$ ($1 \le n \le 5 \cdot 10^5$) — the number of elements in $a$.

The second line of the input contains $n$ integers $a_1, a_2, \dots, a_n$ (each $a_i$ is one of the following numbers: $4, 8, 15, 16, 23, 42$), where $a_i$ is the $i$-th element of $a$.


-----Output-----

Print one integer — the minimum number of elements you have to remove to obtain a good array.


-----Examples-----
Input
5
4 8 15 16 23

Output
5

Input
12
4 8 4 15 16 8 23 15 16 42 23 42

Output
0

Input
15
4 8 4 8 15 16 8 16 23 15 16 4 42 23 42

Output
3
"""

def min_removals_to_make_good_array(n, a):
    f = [4, 8, 15, 16, 23, 42]
    x = [0 for _ in range(6)]
    
    # Map the elements to their respective indices
    for i in range(n):
        if a[i] == 4:
            a[i] = 0
        elif a[i] == 8:
            a[i] = 1
        elif a[i] == 15:
            a[i] = 2
        elif a[i] == 16:
            a[i] = 3
        elif a[i] == 23:
            a[i] = 4
        elif a[i] == 42:
            a[i] = 5
        else:
            a[i] = 6
    
    # Process the array to count valid sequences
    for i in a:
        if i >= 6:
            continue
        if i == 0:
            x[0] += 1
        elif x[i - 1] > 0:
            x[i - 1] -= 1
            x[i] += 1
    
    # Calculate the minimum number of removals
    return n - x[-1] * 6