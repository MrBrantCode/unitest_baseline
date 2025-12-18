"""
QUESTION:
You are given an array $a$ consisting of $n$ integers. Indices of the array start from zero (i. e. the first element is $a_0$, the second one is $a_1$, and so on).

You can reverse at most one subarray (continuous subsegment) of this array. Recall that the subarray of $a$ with borders $l$ and $r$ is $a[l; r] = a_l, a_{l + 1}, \dots, a_{r}$.

Your task is to reverse such a subarray that the sum of elements on even positions of the resulting array is maximized (i. e. the sum of elements $a_0, a_2, \dots, a_{2k}$ for integer $k = \lfloor\frac{n-1}{2}\rfloor$ should be maximum possible).

You have to answer $t$ independent test cases.


-----Input-----

The first line of the input contains one integer $t$ ($1 \le t \le 2 \cdot 10^4$) — the number of test cases. Then $t$ test cases follow.

The first line of the test case contains one integer $n$ ($1 \le n \le 2 \cdot 10^5$) — the length of $a$. The second line of the test case contains $n$ integers $a_0, a_1, \dots, a_{n-1}$ ($1 \le a_i \le 10^9$), where $a_i$ is the $i$-th element of $a$.

It is guaranteed that the sum of $n$ does not exceed $2 \cdot 10^5$ ($\sum n \le 2 \cdot 10^5$).


-----Output-----

For each test case, print the answer on the separate line — the maximum possible sum of elements on even positions after reversing at most one subarray (continuous subsegment) of $a$.


-----Example-----
Input
4
8
1 7 3 4 7 6 2 9
5
1 2 1 2 1
10
7 8 4 5 7 6 8 9 7 3
4
3 1 2 1

Output
26
5
37
5
"""

def maximize_even_position_sum(a, n):
    # Calculate the initial sum of elements on even positions
    evensum = sum(a[i] for i in range(0, n, 2))
    
    # Helper function to find the maximum subarray sum
    def maxSubArraySum(arr, size):
        max_so_far = 0
        max_ending_here = 0
        for i in range(size):
            max_ending_here = max_ending_here + arr[i]
            if max_ending_here < 0:
                max_ending_here = 0
            elif max_so_far < max_ending_here:
                max_so_far = max_ending_here
        return max_so_far
    
    # Calculate potential gains from reversing subarrays
    x = [a[i] - a[i - 1] for i in range(1, n, 2)]
    y = [a[i] - a[i + 1] if i + 1 < n else 0 for i in range(1, n, 2)]
    
    # Find the maximum gain from reversing subarrays
    p = maxSubArraySum(x, len(x))
    q = maxSubArraySum(y, len(y))
    add = max(p, q)
    
    # If the gain is positive, add it to the initial even sum
    if add > 0:
        evensum += add
    
    return evensum