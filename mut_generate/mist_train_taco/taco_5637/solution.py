"""
QUESTION:
Geek is learning data structures. He wants to learn the trie data structure, but there are a few bit's prerequisites that he must first understand.
Given three bit manipulations functions: XOR, check and setBit.
In XOR function you are given two integers n and m return the xor of n and m.
In check function you are given two integer a and b return 1 if a^{th }bit of b is set otherwise return 0.
In setBit function you are given two integer c and d, set the c^{th }bit of d if not yet set.
Example 1:
Input:
n = 1, m = 2
a = 3, b = 4
c = 5, d = 6
Output: 3 1 38
Explanation: 1 xor 2 = 3, 3^{rd }bit of 4 is set. After setting 5^{th }bit of 6 result is 100110 which in decimal form is 38.
Example 2:
Input: 
n = 7, m = 8
a = 9, b = 10
c = 11, d = 12 
Output: 15 0 2060 
Explanation: 7 xor 8 = 15, 9^{th}^{ }bit of 10 is not set. After setting 11^{th }bit of 12 result is 100000001100 which in decimal form is 2060.
Constraints:
1 <= n <= 10^{5}
1 <= m <= 10^{5}
1 <= a <= 9
1 <= b <= 10^{5}
1 <= c <= 9
1 <= d <= 10^{5}
Your Task:
You don't need to read input or print anything. Your task is to complete three functions XOR(), check() and set().
Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)
"""

def perform_bit_operations(n: int, m: int, a: int, b: int, c: int, d: int) -> tuple:
    # XOR operation
    xor_result = n ^ m
    
    # Check operation
    check_result = (b >> (a - 1)) & 1
    
    # SetBit operation
    set_bit_result = d | (1 << c)
    
    return (xor_result, check_result, set_bit_result)