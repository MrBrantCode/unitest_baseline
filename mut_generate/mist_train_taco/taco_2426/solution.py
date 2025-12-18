"""
QUESTION:
Given is a positive integer N. Consider repeatedly applying the operation below on N:
 - First, choose a positive integer z satisfying all of the conditions below:
 - z can be represented as z=p^e, where p is a prime number and e is a positive integer;
 - z divides N;
 - z is different from all integers chosen in previous operations.
 - Then, replace N with N/z.
Find the maximum number of times the operation can be applied.

-----Constraints-----
 - All values in input are integers.
 - 1 \leq N \leq 10^{12}

-----Input-----
Input is given from Standard Input in the following format:
N

-----Output-----
Print the maximum number of times the operation can be applied.

-----Sample Input-----
24

-----Sample Output-----
3

We can apply the operation three times by, for example, making the following choices:
 - Choose z=2 (=2^1). (Now we have N=12.)
 - Choose z=3 (=3^1). (Now we have N=4.)
 - Choose z=4 (=2^2). (Now we have N=1.)
"""

def max_operations_count(N: int) -> int:
    n, p, score = N, 2, 0
    while p ** 2 <= N:
        e = 1
        while n >= p ** e and n % p ** e == 0:
            n //= p ** e
            score += 1
            e += 1
        else:
            while n >= p and n % p == 0:
                n //= p
            p = p + 1 if p == 2 else p + 2
    if n != 1:
        score += 1
    return score