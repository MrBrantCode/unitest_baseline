"""
QUESTION:
You are given a number $n$ and an array $b_1, b_2, \ldots, b_{n+2}$, obtained according to the following algorithm:

some array $a_1, a_2, \ldots, a_n$ was guessed;

array $a$ was written to array $b$, i.e. $b_i = a_i$ ($1 \le i \le n$);

The $(n+1)$-th element of the array $b$ is the sum of the numbers in the array $a$, i.e. $b_{n+1} = a_1+a_2+\ldots+a_n$;

The $(n+2)$-th element of the array $b$ was written some number $x$ ($1 \le x \le 10^9$), i.e. $b_{n+2} = x$; The

array $b$ was shuffled.

For example, the array $b=[2, 3, 7, 12 ,2]$ it could be obtained in the following ways:

$a=[2, 2, 3]$ and $x=12$;

$a=[3, 2, 7]$ and $x=2$.

For the given array $b$, find any array $a$ that could have been guessed initially.


-----Input-----

The first line contains a single integer $t$ ($1 \le t \le 10^4$). Then $t$ test cases follow.

The first line of each test case contains a single integer $n$ ($1 \le n \le 2 \cdot 10^5$).

The second row of each test case contains $n+2$ integers $b_1, b_2, \ldots, b_{n+2}$ ($1 \le b_i \le 10^9$).

It is guaranteed that the sum of $n$ over all test cases does not exceed $2 \cdot 10^5$.


-----Output-----

For each test case, output:

"-1", if the array $b$ could not be obtained from any array $a$;

$n$ integers $a_1, a_2, \ldots, a_n$, otherwise.

If there are several arrays of $a$, you can output any.


-----Examples-----

Input
4
3
2 3 7 12 2
4
9 1 7 1 6 5
5
18 2 2 3 2 9 2
3
2 6 9 2 1
Output
2 3 7 
-1
2 2 2 3 9 
1 2 6


-----Note-----

None
"""

def find_original_array(n, b):
    """
    Given a number n and an array b of size n+2, this function attempts to find the original array a
    that could have been guessed initially. If such an array cannot be found, it returns -1.

    Parameters:
    - n (int): The size of the original array a.
    - b (list of int): The array b of size n+2.

    Returns:
    - list of int: The original array a if it can be found.
    - int: -1 if no valid array a can be found.
    """
    from collections import defaultdict

    # Create a frequency dictionary for elements in b
    freq = defaultdict(int)
    for num in b:
        freq[num] += 1

    # Calculate the sum of all elements in b
    total_sum = sum(b)

    # Iterate over each element in b to check for possible solutions
    for num in b:
        # Decrease the frequency of the current element
        freq[num] -= 1
        # Calculate the potential sum of array a
        potential_sum = total_sum - num
        # Check if the potential sum is even and if the half of it exists in the frequency dictionary
        if potential_sum % 2 == 0:
            potential_sum //= 2
            if freq[potential_sum] > 0:
                # Decrease the frequency of the potential sum element
                freq[potential_sum] -= 1
                # Construct the original array a
                a = []
                for k, v in freq.items():
                    a.extend([k] * v)
                return a
        # Restore the frequency of the current element for the next iteration
        freq[num] += 1

    # If no valid array a is found, return -1
    return -1