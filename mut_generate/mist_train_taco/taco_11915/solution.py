"""
QUESTION:
A number k is called a square number if for some value of d > 1,  k % (d*d) = 0.
Given a number N, find the total number of positive square numbers less than or equal to N.
 
Example 1:
Input:
N = 3
Output:
0
Explanation:
There are no square numbers which
are less than or equal to 3.
Example 2:
Input:
N = 4
Output:
1
Explanation:
4 is the only square number less than
or equal to 4.
4 is divisible by (2*2).
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function sqNum() which takes an Integer N as input and returns the number of square numbers less tha or equal to N.
 
Expected Time Complexity: O(sqrt(N)*log(N) )
Expected Auxiliary Space: O(sqrt(N))
 
Constraints:
1 <= N <= 10^{9}
"""

def count_square_numbers(N):
    def Sieve(n):
        a = [True] * (n + 1)
        primes = []
        a[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if a[i]:
                for j in range(2 * i, n + 1, i):
                    a[j] = False
        for i in range(2, n + 1):
            if a[i]:
                primes.append(i)
        return primes

    def calc(in_, cur, k, primes):
        newCur = primes[in_] * primes[in_] * cur
        res = 0
        if newCur > k:
            return 0
        res += k // newCur
        res += calc(in_ + 1, cur, k, primes)
        res -= calc(in_ + 1, newCur, k, primes)
        return res

    primes = Sieve(100000)
    ans = calc(0, 1, N, primes)
    return ans