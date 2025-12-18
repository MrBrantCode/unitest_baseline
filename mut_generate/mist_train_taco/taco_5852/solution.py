"""
QUESTION:
YouKn0wWho has an integer sequence a_1, a_2, …, a_n. He will perform the following operation until the sequence becomes empty: select an index i such that 1 ≤ i ≤ |a| and a_i is not divisible by (i + 1), and erase this element from the sequence. Here |a| is the length of sequence a at the moment of operation. Note that the sequence a changes and the next operation is performed on this changed sequence.

For example, if a=[3,5,4,5], then he can select i = 2, because a_2 = 5 is not divisible by i+1 = 3. After this operation the sequence is [3,4,5].

Help YouKn0wWho determine if it is possible to erase the whole sequence using the aforementioned operation.

Input

The first line contains a single integer t (1 ≤ t ≤ 10 000) — the number of test cases.

The first line of each test case contains a single integer n (1 ≤ n ≤ 10^5).

The second line of each test case contains n integers a_1, a_2, …, a_n (1 ≤ a_i ≤ 10^9).

It is guaranteed that the sum of n over all test cases doesn't exceed 3 ⋅ 10^5.

Output

For each test case, print "YES" (without quotes) if it is possible to erase the whole sequence using the aforementioned operation, print "NO" (without quotes) otherwise. You can print each letter in any register (upper or lower).

Example

Input


5
3
1 2 3
1
2
2
7 7
10
384836991 191890310 576823355 782177068 404011431 818008580 954291757 160449218 155374934 840594328
8
6 69 696 69696 696969 6969696 69696969 696969696


Output


YES
NO
YES
YES
NO

Note

In the first test case, YouKn0wWho can perform the following operations (the erased elements are underlined): [1, \underline{2}, 3] → [\underline{1}, 3] → [\underline{3}] → [ ].

In the second test case, it is impossible to erase the sequence as i can only be 1, and when i=1, a_1 = 2 is divisible by i + 1 = 2.
"""

def can_erase_sequence(A: list) -> str:
    """
    Determines if the sequence A can be fully erased using the specified operation.

    Parameters:
    A (list): The sequence of integers to be checked.

    Returns:
    str: "YES" if the sequence can be fully erased, "NO" otherwise.
    """
    n = len(A)
    if A[0] % 2 == 0:
        return 'NO'
    x = 2
    for i in range(1, n):
        g = gcd(x, i + 2)
        x = x * (i + 2) // g
        if A[i] % x == 0:
            return 'NO'
        if x > 10 ** 9:
            break
    return 'YES'

def gcd(a: int, b: int) -> int:
    """
    Computes the greatest common divisor (GCD) of two integers a and b.

    Parameters:
    a (int): The first integer.
    b (int): The second integer.

    Returns:
    int: The GCD of a and b.
    """
    if a > b:
        (a, b) = (b, a)
    if b % a == 0:
        return a
    return gcd(b % a, a)