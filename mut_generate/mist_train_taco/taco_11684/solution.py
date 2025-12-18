"""
QUESTION:
For a given string of binary number bi. Find the two’s complement of it.
Example 1:
Input: bi = 00000101
Output: 11111011
Explaination: 2's complement is reversing all 
the bits of the given number and then adding 
1 to it.
Example 2:
Input: bi = 101
Output: 011
Explaination: Follow the process of figuring 
out 2's complement. This will be the answer.
Your Task:
You do not need to read input or print anything. Your task is to complete the function complement() which takes bi as input parameter and returns the 2's complement of the number.
Expected Time Complexity: O(|bi|)
Expected Auxiliary Space: O(|bi|)
Constraints:
1 ≤ |bi| ≤ 10
"""

def twos_complement(bi: str) -> str:
    # Step 1: Reverse the bits
    reversebi = ''.join('1' if bit == '0' else '0' for bit in bi)
    
    # Step 2: Add 1 to the reversed bits
    carry = 1
    twos_complement = ''
    for bit in reversebi[::-1]:
        if bit == '0' and carry == 1:
            twos_complement += '1'
            carry = 0
        elif bit == '1' and carry == 1:
            twos_complement += '0'
        else:
            twos_complement += bit
    
    # Step 3: Reverse the result to get the final two's complement
    return twos_complement[::-1]