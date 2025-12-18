"""
QUESTION:
Let's define the value of the permutation $p$ of $n$ integers $1$, $2$, ..., $n$ (a permutation is an array where each element from $1$ to $n$ occurs exactly once) as follows:

initially, an integer variable $x$ is equal to $0$;

if $x < p_1$, then add $p_1$ to $x$ (set $x = x + p_1$), otherwise assign $0$ to $x$;

if $x < p_2$, then add $p_2$ to $x$ (set $x = x + p_2$), otherwise assign $0$ to $x$;

...

if $x < p_n$, then add $p_n$ to $x$ (set $x = x + p_n$), otherwise assign $0$ to $x$;

the value of the permutation is $x$ at the end of this process.

For example, for $p = [4, 5, 1, 2, 3, 6]$, the value of $x$ changes as follows: $0, 4, 9, 0, 2, 5, 11$, so the value of the permutation is $11$.

You are given an integer $n$. Find a permutation $p$ of size $n$ with the maximum possible value among all permutations of size $n$. If there are several such permutations, you can print any of them.


-----Input-----

The first line contains one integer $t$ ($1 \le t \le 97$) — the number of test cases.

The only line of each test case contains one integer $n$ ($4 \le n \le 100$).


-----Output-----

For each test case, print $n$ integers — the permutation $p$ of size $n$ with the maximum possible value among all permutations of size $n$.


-----Examples-----

Input
3
4
5
6
Output
2 1 3 4
1 2 3 4 5
4 5 1 2 3 6


-----Note-----

None
"""

def find_max_value_permutations(t: int, n_list: list) -> list:
    """
    Finds permutations of size n with the maximum possible value for each test case.

    Parameters:
    t (int): The number of test cases.
    n_list (list): A list of integers where each integer represents the size of the permutation for a test case.

    Returns:
    list: A list of lists, where each inner list is a permutation of size n with the maximum possible value.
    """
    result = []
    for n in n_list:
        if n % 2 == 0:
            arr = [k for k in range(n - 2, 0, -1)]
            arr += [n - 1, n]
        else:
            arr = [1, 2, 3]
            arr += [k for k in range(n - 2, 3, -1)]
            arr += [n - 1, n]
        result.append(arr)
    return result