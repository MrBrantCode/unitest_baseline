"""
QUESTION:
Today Hayato came home from school with homework.

In the assignment, Hayato was given an array $a$ of length $n$. The task was to find $3$ numbers in this array whose sum is odd. At school, he claimed that there are such $3$ numbers, but Hayato was not sure, so he asked you for help.

Answer if there are such three numbers, and if so, output indices $i$, $j$, and $k$ such that $a_i + a_j + a_k$ is odd.

The odd numbers are integers that are not divisible by $2$: $1$, $3$, $5$, and so on.


-----Input-----

The first line contains a single integer $t$ ($1 \le t \le 10^4$) — the number of test cases.

For each test case, the first line contains one integer $n$ ($3 \le n \le 300$) — the length of $a$.

The second line contains $n$ integers $a_1, a_2, \ldots, a_n$ ($1 \le a_i \le 10^5$) — the array $a$.

It is guaranteed that the sum of $n$ over all test cases does not exceed $2\cdot10^5$.


-----Output-----

For each test case, in the first line print one word "YES" (without quotes) if there are $3$ numbers with an odd sum or "NO" (without quotes) if there are no such $3$ numbers.

If the answer exists, then on the second line print $3$ distinct integers $i, j, k$ ($1 \le i, j, k \le n$) — the indices of the numbers. If there are several answers, output any.


-----Examples-----

Input
6
3
1 1 1
4
1 1 2 2
3
1 2 3
5
1 4 5 1 2
4
2 6 2 4
5
5 6 3 2 1
Output
YES
1 2 3
YES
3 4 1
NO
YES
1 3 4
NO
YES
1 3 5


-----Note-----

In the first test case, there is one way to choose $3$ numbers, and since $1 + 1 + 1 = 3$, this triple is fine for us.

In the second test case, you need to choose the numbers $1, 2, 2$, since $1 + 2 + 2 = 5$.

In the third test case, there is one way to choose three numbers, but $1 + 2 + 3 = 6$ is an even number, so the required triple does not exist.

In the fifth test case, no matter what three numbers we choose, their sum is even.
"""

def find_odd_sum_triplet(n, a):
    """
    Finds three numbers in the array `a` of length `n` whose sum is odd.

    Parameters:
    - n (int): The length of the array `a`.
    - a (list of int): The array of integers.

    Returns:
    - tuple: A tuple where the first element is a boolean indicating whether such a triplet exists.
             If the boolean is True, the second element is a tuple of three indices (i, j, k) such that a[i] + a[j] + a[k] is odd.
             If the boolean is False, the second element is None.
    """
    idx1 = []  # Indices of odd numbers
    idx2 = []  # Indices of even numbers
    
    for i in range(n):
        if a[i] % 2 == 1:
            idx1.append(i + 1)
        else:
            idx2.append(i + 1)
    
    if len(idx1) == 0:
        return (False, None)
    elif len(idx1) == 1:
        if len(idx2) >= 2:
            return (True, (idx1[0], idx2[0], idx2[1]))
        else:
            return (False, None)
    elif len(idx1) == 2:
        if len(idx2) >= 1:
            return (True, (idx1[0], idx2[0], idx2[1]))
        else:
            return (False, None)
    else:
        return (True, (idx1[0], idx1[1], idx1[2]))