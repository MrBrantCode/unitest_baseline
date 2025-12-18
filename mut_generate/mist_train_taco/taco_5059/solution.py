"""
QUESTION:
Given n and k, Construct a palindrome of size n using the binary representation of the number k.To construct the palindrome you can use the binary number of size k as many times as you wish and also you can trim all the  zeros from the end.The palindrome must always begin with 1 and contains the maximum number of zeros.
 
Example 1 :
Input : n = 5, k = 6
Output : 11011
Explanation: Binary representation of 6 is
110.After combining 110
twice and trimming the extra 0 in 
the end we get 11011
Example 2:
Input: n = 5, k = 8
Output: 10001
Explanation: Binary representation of 8 is
1000.After combining 1000 twice and trimming
the extra 0 in the end we get 10001.
Your Task:
You don't need to read or print anything. Your task is to complete the function binaryPalindrome() that takes two integers n, k and return a string of size n.
Expected Time Complexity: O(n).
Expected Auxiliary Space: O(1).
Constraints:
1 ≤ n ≤ 10^{5}
1 ≤ k ≤ 10^{5}
"""

def binary_palindrome(n: int, k: int) -> str:
    # Convert k to its binary representation and remove the '0b' prefix
    binary_k = bin(k)[2:]
    
    # Initialize the palindrome with zeros
    palindrome = ['0'] * n
    
    # Ensure the palindrome starts with '1'
    palindrome[0] = '1'
    palindrome[-1] = '1'
    
    # Fill the palindrome with the binary representation of k
    for i in range(1, (n // 2) + 1):
        if i < len(binary_k):
            palindrome[i] = binary_k[i]
            palindrome[-i-1] = binary_k[i]
        else:
            palindrome[i] = '0'
            palindrome[-i-1] = '0'
    
    # Convert the list back to a string
    return ''.join(palindrome)