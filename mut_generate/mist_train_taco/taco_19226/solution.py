"""
QUESTION:
Anu has created her own function $f$: $f(x, y) = (x | y) - y$ where $|$ denotes the bitwise OR operation. For example, $f(11, 6) = (11|6) - 6 = 15 - 6 = 9$. It can be proved that for any nonnegative numbers $x$ and $y$ value of $f(x, y)$ is also nonnegative. 

She would like to research more about this function and has created multiple problems for herself. But she isn't able to solve all of them and needs your help. Here is one of these problems.

A value of an array $[a_1, a_2, \dots, a_n]$ is defined as $f(f(\dots f(f(a_1, a_2), a_3), \dots a_{n-1}), a_n)$ (see notes). You are given an array with not necessarily distinct elements. How should you reorder its elements so that the value of the array is maximal possible?


-----Input-----

The first line contains a single integer $n$ ($1 \le n \le 10^5$).

The second line contains $n$ integers $a_1, a_2, \ldots, a_n$ ($0 \le a_i \le 10^9$). Elements of the array are not guaranteed to be different.


-----Output-----

Output $n$ integers, the reordering of the array with maximum value. If there are multiple answers, print any.


-----Examples-----
Input
4
4 0 11 6

Output
11 6 4 0
Input
1
13

Output
13 


-----Note-----

In the first testcase, value of the array $[11, 6, 4, 0]$ is $f(f(f(11, 6), 4), 0) = f(f(9, 4), 0) = f(9, 0) = 9$.

$[11, 4, 0, 6]$ is also a valid answer.
"""

def maximize_array_value(arr):
    n = len(arr)
    if n == 1:
        return arr
    
    # Initialize an array to store intermediate results
    p = [0] * n
    
    # Calculate the intermediate values
    temp = ~arr[0]
    for i in range(1, n):
        p[i] = temp
        temp &= ~arr[i]
    
    temp = ~arr[-1]
    ans = [-1, -float('inf')]
    
    for i in range(n - 2, -1, -1):
        if i != 0:
            p[i] &= temp
            temp &= ~arr[i]
            p[i] &= arr[i]
            if ans[1] < p[i]:
                ans[0] = i
                ans[1] = p[i]
        else:
            p[i] = arr[i] & temp
            if ans[1] < p[i]:
                ans[0] = i
                ans[1] = p[i]
    
    p[-1] &= arr[-1]
    if ans[1] < p[-1]:
        ans[0] = n - 1
        ans[1] = p[-1]
    
    # Reorder the array with the maximal value
    reordered_arr = [arr[ans[0]]] + [arr[i] for i in range(n) if i != ans[0]]
    
    return reordered_arr