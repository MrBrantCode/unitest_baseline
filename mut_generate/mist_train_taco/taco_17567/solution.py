"""
QUESTION:
For two given positive numbers a and b. Find a^{b}. Output your number modulus 10^{9}+7.
Example 1:
Input: a = 1, b = 1
Output: 1
Explanation: 1^{1} % (10^{9}+7) = 1
Ã¢â¬â¹Example 2:
Input: a = 2, b = 5
Output: 32
Explanation: 2^{5} % (10^{9}+7) = 32
Your Task:  
You don't need to read input or print anything. Your task is to complete the function power() which takes a, b as inputs, and returns the answer.
Expected Time Complexity: O(log b)
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ a ≤ 10^{5}
1 ≤ b ≤ 10^{16}
"""

def modular_exponentiation(a: int, b: int) -> int:
    """
    Calculate a^b % (10^9 + 7) efficiently using modular exponentiation.

    Parameters:
    a (int): The base number.
    b (int): The exponent.

    Returns:
    int: The result of a^b % (10^9 + 7).
    """
    mod = 10**9 + 7
    ans = 1
    
    # Handle negative exponent if needed (not required by the problem constraints)
    neg = False
    if b < 0:
        neg = True
        b = -b
    
    while b != 0:
        if b % 2:
            ans = ans * a % mod
            b -= 1
        else:
            a = a * a % mod
            b //= 2
    
    if neg:
        ans = pow(ans, -1, mod)
    
    return ans % mod