"""
QUESTION:
Given a number N.Check if it is Full Prime or not. 
Note : A full prime number is one in which the number itself is prime and all its digits are also prime.
Example 1:
Input:
N=31
Output:
0
Explanation:
N is prime but since 1 is not a 
prime so all the digits of N
are not prime.So, Answer is 0.
Example 2:
Input:
N=37
Output:
1
Explanation:
N is prime and so is all of its digits.
Thus, Answer is 1.
Your Task:
You don't need to read input or print anything.Your task is to complete the function fullPrime() which takes the number N as input parameter and returns 1 if the number is Full Prime.Otherwise return 0.
Expected Time Complexity:O(Sqrt(N))
Expected Auxillary Space:O(1)
Constraints:
1<=N<=10^{9}
"""

def is_full_prime(N: int) -> int:
    def is_prime(num: int) -> bool:
        if num < 2:
            return False
        i = 2
        while i * i <= num:
            if num % i == 0:
                return False
            i += 1
        return True

    if not is_prime(N):
        return 0

    while N > 0:
        digit = N % 10
        if digit not in {2, 3, 5, 7}:
            return 0
        N //= 10

    return 1