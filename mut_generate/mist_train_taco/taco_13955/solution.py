"""
QUESTION:
The problem set at CODE FESTIVAL 20XX Finals consists of N problems.

The score allocated to the i-th (1≦i≦N) problem is i points.

Takahashi, a contestant, is trying to score exactly N points. For that, he is deciding which problems to solve.

As problems with higher scores are harder, he wants to minimize the highest score of a problem among the ones solved by him.

Determine the set of problems that should be solved.

Constraints

* 1≦N≦10^7

Input

The input is given from Standard Input in the following format:


N


Output

Among the sets of problems with the total score of N, find a set in which the highest score of a problem is minimum, then print the indices of the problems in the set in any order, one per line.

If there exists more than one such set, any of them will be accepted.

Examples

Input

4


Output

1
3


Input

7


Output

1
2
4


Input

1


Output

1
"""

def find_minimum_highest_score_problems(N: int) -> list:
    # Find the smallest n such that the sum of the first n natural numbers is at least N
    for n in range(1, N + 1):
        if n * (n + 1) // 2 >= N:
            break
    
    # Calculate the difference between the sum of the first n natural numbers and N
    d = n * (n + 1) // 2 - N
    
    # Create a set of the first n natural numbers
    s = set(range(1, n + 1))
    
    # Remove the difference from the set if it exists
    s.discard(d)
    
    # Convert the set to a list and return
    return list(s)