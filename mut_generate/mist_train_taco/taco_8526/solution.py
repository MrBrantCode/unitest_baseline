"""
QUESTION:
One quite ordinary day Valera went to school (there's nowhere else he should go on a week day). In a maths lesson his favorite teacher Ms. Evans told students about divisors. Despite the fact that Valera loved math, he didn't find this particular topic interesting. Even more, it seemed so boring that he fell asleep in the middle of a lesson. And only a loud ringing of a school bell could interrupt his sweet dream.

Of course, the valuable material and the teacher's explanations were lost. However, Valera will one way or another have to do the homework. As he does not know the new material absolutely, he cannot do the job himself. That's why he asked you to help. You're his best friend after all, you just cannot refuse to help.

Valera's home task has only one problem, which, though formulated in a very simple way, has not a trivial solution. Its statement looks as follows: if we consider all positive integers in the interval [a;b] then it is required to count the amount of such numbers in this interval that their smallest divisor will be a certain integer k (you do not have to consider divisor equal to one). In other words, you should count the amount of such numbers from the interval [a;b], that are not divisible by any number between 2 and k - 1 and yet are divisible by k. 

Input

The first and only line contains three positive integers a, b, k (1 ≤ a ≤ b ≤ 2·109, 2 ≤ k ≤ 2·109). 

Output

Print on a single line the answer to the given problem. 

Examples

Input

1 10 2


Output

5


Input

12 23 3


Output

2


Input

6 19 5


Output

0

Note

Comments to the samples from the statement: 

In the first sample the answer is numbers 2, 4, 6, 8, 10.

In the second one — 15, 21

In the third one there are no such numbers.
"""

def is_prime(x):
    """Helper function to check if a number is prime."""
    if x < 2:
        return False
    d = 2
    while d * d <= x:
        if x % d == 0:
            return False
        d += 1
    return True

def count_numbers_with_smallest_divisor(a, b, k):
    """
    Counts the number of integers in the interval [a, b] that have k as their smallest divisor.
    
    Parameters:
    a (int): The start of the interval (inclusive).
    b (int): The end of the interval (inclusive).
    k (int): The specific divisor that should be the smallest divisor for the numbers in the interval.
    
    Returns:
    int: The count of such numbers.
    """
    if not is_prime(k) or b < k:
        return 0
    
    def count_divisible_by_k(n, k):
        """Helper function to count numbers up to n that are divisible by k."""
        if n < k:
            return 0
        n1 = n // k
        return n1 - sum((count_divisible_by_k(n1, i) for i in range(2, min(k, n1 + 1))))
    
    return count_divisible_by_k(b, k) - count_divisible_by_k(a - 1, k)