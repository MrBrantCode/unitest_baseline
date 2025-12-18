"""
QUESTION:
Given a number n, the task is to find out whether this number is a Smith Number or not. A Smith Number is a composite number whose sum of digits is equal to the sum of digits of its prime factorization.
 
Example 1:
Input:
n = 4
Output:
1
Explanation:
Prime factorization = 2, 2; and 2 + 2 = 4
Therefore, 4 is a Smith Number.
Example 2:
Input:
n = 6
Output:
0
Explanation:
Prime factorization = 2, 3; and 2 + 3 is
not 6. Therefore, 6 is Not a Smith Number.
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function smithNum() which takes an Integer n as input and returns the answer.
 
Expected Time Complexity: O(n)
Expected Auxiliary Space: O(n)
 
Constraints:
1 <= n <= 10^{5}
"""

def is_smith_number(n: int) -> int:
    def is_prime(num: int) -> bool:
        if num == 0 or num == 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    if is_prime(n):
        return 0

    digit_sum = sum(map(int, str(n)))
    prime_factor_sum = 0
    divisor = 2

    while n > 1:
        if n % divisor == 0:
            n //= divisor
            prime_factor_sum += sum(map(int, str(divisor)))
        else:
            divisor += 1

    return 1 if prime_factor_sum == digit_sum else 0