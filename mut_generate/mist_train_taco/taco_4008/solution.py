"""
QUESTION:
A sequence a=\{a_1,a_2,a_3,......\} is determined as follows:
 - The first term s is given as input.
 - Let f(n) be the following function: f(n) = n/2 if n is even, and f(n) = 3n+1 if n is odd.
 - a_i = s when i = 1, and a_i = f(a_{i-1}) when i > 1.
Find the minimum integer m that satisfies the following condition:
 - There exists an integer n such that a_m = a_n (m > n).

-----Constraints-----
 - 1 \leq s \leq 100
 - All values in input are integers.
 - It is guaranteed that all elements in a and the minimum m that satisfies the condition are at most 1000000.

-----Input-----
Input is given from Standard Input in the following format:
s

-----Output-----
Print the minimum integer m that satisfies the condition.

-----Sample Input-----
8

-----Sample Output-----
5

a=\{8,4,2,1,4,2,1,4,2,1,......\}. As a_5=a_2, the answer is 5.
"""

def find_minimum_cycle_length(s: int) -> int:
    """
    Finds the minimum integer m that satisfies the condition:
    There exists an integer n such that a_m = a_n (m > n) in the sequence defined by:
    - a_1 = s
    - a_i = f(a_{i-1}) for i > 1, where f(n) = n/2 if n is even, and f(n) = 3n+1 if n is odd.

    Parameters:
    s (int): The starting integer of the sequence.

    Returns:
    int: The minimum integer m that satisfies the condition.
    """
    vs = set()
    vs.add(s)
    now = s
    i = 1
    while True:
        i += 1
        now = now // 2 if now % 2 == 0 else 3 * now + 1
        if now in vs:
            return i
        else:
            vs.add(now)