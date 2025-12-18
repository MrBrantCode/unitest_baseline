"""
QUESTION:
Given a number N, the task is to express N as a summation of 4 positive primes.
 
Example 1:
Input: N = 8
Output: 2 2 2 2
Explanation: 2 is prime and 2 + 2 + 2 + 2 = 8
Example 2:
Input: N = 15
Output: 2 3 3 7
Explanation: 2, 3 and 7 are prime and 2 + 3 + 
+ 3 + 7 = 15.
 
Your Task:
You don't need to read or print anything. Your task is to complete the function Express() which takes N as input parameter and returns a list of four number if N can be expressed as a summation of four numbers otherwise returns a list containing -1. The returned list should be in increasing order. If there are more than one list possible then returns the lexicograhically smallest one.
 
Expected Time Complexity: O(N*log(N))
Expected Space Complexity: O(N)
Constraints:
1 <= N <= 10^{5}
"""

def express_as_sum_of_four_primes(N: int) -> list:
    def is_prime(num: int) -> bool:
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def find_other_two_primes(num: int) -> list:
        for i in range(2, num // 2 + 1):
            if is_prime(i) and is_prime(num - i):
                return [i, num - i]
        return [-1]

    if N < 8:
        return [-1]
    
    if N % 2 == 0:
        result = [2, 2]
        result.extend(find_other_two_primes(N - 4))
    else:
        result = [2, 3]
        result.extend(find_other_two_primes(N - 5))
    
    return sorted(result)