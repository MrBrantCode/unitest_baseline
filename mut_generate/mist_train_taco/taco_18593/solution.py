"""
QUESTION:
Given an even number N (greater than 2), return two prime numbers whose sum will be equal to given number. There are several combinations possible. Print only the pair whose minimum value is the smallest among all the minimum values of pairs and print the minimum element first.
NOTE: A solution will always exist, read Goldbachs conjecture. 
Example 1:
Input: N = 74
Output: 3 71
Explaination: There are several possibilities 
like 37 37. But the minimum value of this pair 
is 3 which is smallest among all possible 
minimum values of all the pairs.
Example 2:
Input: 4
Output: 2 2
Explaination: This is the only possible 
prtitioning of 4.
Your Task:
You do not need to read input or print anything. Your task is to complete the function primeDivision() which takes N as input parameter and returns the partition satisfying the condition.
Expected Time Complexity: O(N*log(logN))
Expected Auxiliary Space: O(N)
Constraints:
4 ≤ N ≤ 10^{4}
"""

def find_prime_pair(N):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    for i in range(2, N // 2 + 1):
        if is_prime(i) and is_prime(N - i):
            return (i, N - i)

    # Since a solution always exists (Goldbach's conjecture), this line should never be reached.
    return None