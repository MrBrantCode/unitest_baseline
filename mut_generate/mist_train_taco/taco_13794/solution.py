"""
QUESTION:
You are given integers N and M.
Consider a sequence a of length N consisting of positive integers such that a_1 + a_2 + ... + a_N = M. Find the maximum possible value of the greatest common divisor of a_1, a_2, ..., a_N.

-----Constraints-----
 - All values in input are integers.
 - 1 \leq N \leq 10^5
 - N \leq M \leq 10^9

-----Input-----
Input is given from Standard Input in the following format:
N M

-----Output-----
Print the maximum possible value of the greatest common divisor of a sequence a_1, a_2, ..., a_N that satisfies the condition.

-----Sample Input-----
3 14

-----Sample Output-----
2

Consider the sequence (a_1, a_2, a_3) = (2, 4, 8). Their greatest common divisor is 2, and this is the maximum value.
"""

def max_gcd_of_sequence(N, M):
    def make_divisors(n):
        (lower_divisors, upper_divisors) = ([], [])
        i = 1
        while i * i <= n:
            if n % i == 0:
                lower_divisors.append(i)
                if i != n // i:
                    upper_divisors.append(n // i)
            i += 1
        return lower_divisors + upper_divisors[::-1]
    
    ans = 0
    for i in make_divisors(M):
        if M // i >= N:
            ans = i
    return ans