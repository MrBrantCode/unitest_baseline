"""
QUESTION:
Given an array $a$ consisting of $n$ elements, find the maximum possible sum the array can have after performing the following operation any number of times:

Choose $2$ adjacent elements and flip both of their signs. In other words choose an index $i$ such that $1 \leq i \leq n - 1$ and assign $a_i = -a_i$ and $a_{i+1} = -a_{i+1}$.


-----Input-----

The input consists of multiple test cases. The first line contains an integer $t$ ($1 \leq t \leq 1000$) — the number of test cases. The descriptions of the test cases follow.

The first line of each test case contains an integer $n$ ($2 \leq n \leq 2\cdot10^5$) — the length of the array.

The following line contains $n$ space-separated integers $a_1,a_2,\dots,a_n$ ($-10^9 \leq a_i \leq 10^9$).

It is guaranteed that the sum of $n$ over all test cases does not exceed $2\cdot10^5$.


-----Output-----

For each test case, output the maximum possible sum the array can have after performing the described operation any number of times.


-----Examples-----

Input
5
3
-1 -1 -1
5
1 5 -5 0 2
3
1 2 3
6
-1 10 9 8 7 6
2
-1 -1
Output
1
13
6
39
2


-----Note-----

For the first test case, by performing the operation on the first two elements, we can change the array from $[-1, -1, -1]$ to $[1, 1, -1]$, and it can be proven this array obtains the maximum possible sum which is $1 + 1 + (-1) = 1$.

For the second test case, by performing the operation on $-5$ and $0$, we change the array from $[1, 5, -5, 0, 2]$ to $[1, 5, -(-5), -0, 2] = [1, 5, 5, 0, 2]$, which has the maximum sum since all elements are non-negative. So, the answer is $1 + 5 + 5 + 0 + 2 = 13$.

For the third test case, the array already contains only positive numbers, so performing operations is unnecessary. The answer is just the sum of the whole array, which is $1 + 2 + 3 = 6$.
"""

def max_possible_sum_after_flips(a):
    # Convert all elements to their absolute values
    a = list(map(abs, a))
    
    # Calculate the sum of the absolute values
    total_sum = sum(a)
    
    # Count the number of negative signs in the original array
    negative_count = sum(1 for x in a if x < 0)
    
    # If there are an odd number of negative signs, we need to flip one pair
    if negative_count % 2 != 0:
        # Subtract twice the minimum absolute value to account for the flip
        total_sum -= 2 * min(a)
    
    return total_sum