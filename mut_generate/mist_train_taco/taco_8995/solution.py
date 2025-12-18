"""
QUESTION:
You are given a binary string of length $n$ (i. e. a string consisting of $n$ characters '0' and '1').

In one move you can swap two adjacent characters of the string. What is the lexicographically minimum possible string you can obtain from the given one if you can perform no more than $k$ moves? It is possible that you do not perform any moves at all.

Note that you can swap the same pair of adjacent characters with indices $i$ and $i+1$ arbitrary (possibly, zero) number of times. Each such swap is considered a separate move.

You have to answer $q$ independent test cases.


-----Input-----

The first line of the input contains one integer $q$ ($1 \le q \le 10^4$) — the number of test cases.

The first line of the test case contains two integers $n$ and $k$ ($1 \le n \le 10^6, 1 \le k \le n^2$) — the length of the string and the number of moves you can perform.

The second line of the test case contains one string consisting of $n$ characters '0' and '1'.

It is guaranteed that the sum of $n$ over all test cases does not exceed $10^6$ ($\sum n \le 10^6$).


-----Output-----

For each test case, print the answer on it: the lexicographically minimum possible string of length $n$ you can obtain from the given one if you can perform no more than $k$ moves.


-----Example-----
Input
3
8 5
11011010
7 9
1111100
7 11
1111100

Output
01011110
0101111
0011111



-----Note-----

In the first example, you can change the string as follows: $1\underline{10}11010 \rightarrow \underline{10}111010 \rightarrow 0111\underline{10}10 \rightarrow 011\underline{10}110 \rightarrow 01\underline{10}1110 \rightarrow 01011110$. 

In the third example, there are enough operations to make the string sorted.
"""

def minimize_binary_string(n, k, s):
    """
    Given a binary string of length `n`, this function returns the lexicographically minimum possible string
    that can be obtained by performing no more than `k` adjacent swaps.

    Parameters:
    - n (int): The length of the binary string.
    - k (int): The maximum number of moves allowed.
    - s (str): The binary string consisting of '0's and '1's.

    Returns:
    - str: The lexicographically minimum possible string after performing no more than `k` moves.
    """
    s = list(s)  # Convert the string to a list for easier manipulation
    l = ['1'] * n  # Initialize the result list with '1's
    ind = 0  # Index to track the position of the next '0' to be placed

    for i in range(n):
        if s[i] == '0':
            val = min(k, i - ind)  # Calculate the number of moves we can make
            k -= val  # Decrease the number of available moves
            l[i - val] = '0'  # Place '0' at the new position
            ind += 1  # Increment the index for the next '0'

    return ''.join(l)  # Convert the list back to a string and return