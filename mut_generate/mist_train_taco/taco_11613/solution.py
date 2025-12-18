"""
QUESTION:
You are given n integers a_1, a_2, …, a_n and an integer k. Find the maximum value of i ⋅ j - k ⋅ (a_i | a_j) over all pairs (i, j) of integers with 1 ≤ i < j ≤ n. Here, | is the [bitwise OR operator](https://en.wikipedia.org/wiki/Bitwise_operation#OR).

Input

The first line contains a single integer t (1 ≤ t ≤ 10 000) — the number of test cases.

The first line of each test case contains two integers n (2 ≤ n ≤ 10^5) and k (1 ≤ k ≤ min(n, 100)).

The second line of each test case contains n integers a_1, a_2, …, a_n (0 ≤ a_i ≤ n).

It is guaranteed that the sum of n over all test cases doesn't exceed 3 ⋅ 10^5.

Output

For each test case, print a single integer — the maximum possible value of i ⋅ j - k ⋅ (a_i | a_j).

Example

Input


4
3 3
1 1 3
2 2
1 2
4 3
0 1 2 3
6 6
3 2 0 0 5 6


Output


-1
-4
3
12

Note

Let f(i, j) = i ⋅ j - k ⋅ (a_i | a_j).

In the first test case, 

  * f(1, 2) = 1 ⋅ 2 - k ⋅ (a_1 | a_2) = 2 - 3 ⋅ (1 | 1) = -1. 
  * f(1, 3) = 1 ⋅ 3 - k ⋅ (a_1 | a_3) = 3 - 3 ⋅ (1 | 3) = -6. 
  * f(2, 3) = 2 ⋅ 3 - k ⋅ (a_2 | a_3) = 6 - 3 ⋅ (1 | 3) = -3. 



So the maximum is f(1, 2) = -1.

In the fourth test case, the maximum is f(3, 4) = 12.
"""

def find_max_value(n, k, arr):
    ans = -10 ** 18
    temp = []
    cnt = 0
    
    # Collect up to 300 elements from the end of the array
    for i in range(n - 1, -1, -1):
        temp.append((arr[i], i))
        cnt += 1
        if cnt == 300:
            break
    
    # Calculate the maximum value for the selected pairs
    for i in range(len(temp)):
        for j in range(i + 1, len(temp)):
            (u1, v1) = temp[i]
            (u2, v2) = temp[j]
            ans = max(ans, (v1 + 1) * (v2 + 1) - k * (u1 | u2))
    
    return ans