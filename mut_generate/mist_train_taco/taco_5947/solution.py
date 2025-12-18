"""
QUESTION:
Given a number N , calculate total number of permutations of it and also the sum of all permutations including that number itself.
 
Example 1:
Input: N = 5
Output: 1 5
Explanation: There is only one permutation
of 5 and sum of this permutaion is 5.
Example 2:
Input: N = 12
Output: 2 33
Explanation: Permutations of 12 are 12 and 21.
Sum of these permutations are = 12 + 21 = 33.
 
Your Task:
You don't need to read or print anyhting. Your task is to complete the function permutation() which takes N as input parameter ans returns a list that contains total number of permutations and sum of all these permutations including the number iteself.
 
Expected Time Complexity: O(K!) where K = log_{10}N
Expected Space Complexity: O(1)
Constraints:
1 <= N <= 10^{5}
"""

def calculate_permutations_and_sum(N):
    def factorial(no):
        ans = 1
        while no > 0:
            ans *= no
            no -= 1
        return ans

    cnt = 1
    dig_sum = 0
    n = N
    n1 = N
    map1 = {}
    
    # Count the number of digits in N
    while N > 9:
        N //= 10
        cnt += 1
    
    no_dig = cnt
    no_dig1 = cnt
    perm = factorial(cnt)
    sum1 = 0
    x = perm // no_dig
    
    # Calculate the sum of permutations
    while no_dig > 0:
        dig = n // 10 ** (no_dig - 1)
        if dig not in map1:
            map1[dig] = 1
        else:
            map1[dig] += 1
        sum1 += dig * x
        n %= 10 ** (no_dig - 1)
        no_dig -= 1
    
    no = 1
    while no_dig1 > 1:
        no += 10 ** (no_dig1 - 1)
        no_dig1 -= 1
    
    final_sum = sum1 * no
    
    # Adjust for repeated digits
    for items in map1.values():
        M = factorial(items)
        perm //= M
        final_sum //= M
    
    return [perm, final_sum]