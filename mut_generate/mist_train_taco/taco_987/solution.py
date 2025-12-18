"""
QUESTION:
This is an interactive problem.

We hid from you a permutation p of length n, consisting of the elements from 1 to n. You want to guess it. To do that, you can give us 2 different indices i and j, and we will reply with p_{i} mod p_{j} (remainder of division p_{i} by p_{j}).

We have enough patience to answer at most 2 ⋅ n queries, so you should fit in this constraint. Can you do it?

As a reminder, a permutation of length n is an array consisting of n distinct integers from 1 to n in arbitrary order. For example, [2,3,1,5,4] is a permutation, but [1,2,2] is not a permutation (2 appears twice in the array) and [1,3,4] is also not a permutation (n=3 but there is 4 in the array).

Input

The only line of the input contains a single integer n (1 ≤ n ≤ 10^4) — length of the permutation.

Interaction

The interaction starts with reading n. 

Then you are allowed to make at most 2 ⋅ n queries in the following way: 

  * "? x y" (1 ≤ x, y ≤ n, x ≠ y). 



After each one, you should read an integer k, that equals p_x mod p_y. 

When you have guessed the permutation, print a single line "! " (without quotes), followed by array p and quit.

After printing a query do not forget to output end of line and flush the output. Otherwise, you will get Idleness limit exceeded. To do this, use:

  * fflush(stdout) or cout.flush() in C++;
  * System.out.flush() in Java;
  * flush(output) in Pascal;
  * stdout.flush() in Python;
  * see documentation for other languages.



Exit immediately after receiving "-1" and you will see Wrong answer verdict. Otherwise you can get an arbitrary verdict because your solution will continue to read from a closed stream.

Hack format

In the first line output n (1 ≤ n ≤ 10^4). In the second line print the permutation of n integers p_1, p_2, …, p_n.

Example

Input


3

1

2

1

0

Output


? 1 2

? 3 2

? 1 3

? 2 1

! 1 3 2
"""

def guess_permutation(n, queries, responses):
    """
    Guesses the permutation of length n using the given queries and responses.

    Parameters:
    - n (int): The length of the permutation.
    - queries (list of tuples): A list of tuples where each tuple contains two indices (i, j) representing the queries made to the permutation.
    - responses (list of int): A list of integers representing the responses to the queries.

    Returns:
    - list of int: The guessed permutation.
    """
    cache = {}
    
    def query(i, j):
        if (i, j) not in cache:
            index = len(cache)
            cache[i, j] = responses[index]
        return cache[i, j]
    
    ans = [-1 for _ in range(n)]
    last = 0
    
    for i in range(1, n):
        a = query(i, last)
        b = query(last, i)
        if a > b:
            ans[i] = a
        else:
            ans[last] = b
            last = i
    
    for i in range(n):
        if ans[i] == -1:
            ans[i] = n
    
    return ans