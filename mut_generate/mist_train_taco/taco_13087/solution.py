"""
QUESTION:
This follows from Game of Thrones - I.

Now that the king knows how to find out whether a given word has an anagram which is a palindrome or not, he encounters another challenge. He realizes that there can be more than one palindrome anagrams for a given word. Can you help him find out how many palindrome anagrams are possible for a given word ?

The king has many words. For each given word, he needs to find out the number of palindrome anagrams of the string. As the number of anagrams can be large, the king needs the number of anagrams % (10^{9}+ 7).

Input format :

A single line which contains the input string

Output format : 

A single line which contains the number of anagram strings which are palindrome % (10^{9} + 7).

Constraints : 

1<=length of string <= 10^5 

Each character of the string is a lowercase alphabet. 

Each test case has at least 1 anagram which is a palindrome. 

Sample Input 01 :

aaabbbb

Sample Output 01 :

3 

Explanation : 

Three palindrome permutations of the given string are abbabba , bbaaabb and bababab.

Sample Input 02 :

cdcdcdcdeeeef

Sample Output 02 :

90
"""

def count_palindrome_anagrams(word: str) -> int:
    MOD = 1000000007
    
    def fact_mod_p_brute(n: int, p: int) -> int:
        if n == 0:
            return 1
        res = 1
        for i in range(1, n + 1):
            res *= i
            res = res % p
        return res
    
    # Initialize frequency array for characters
    freq = [0] * 270
    
    # Count frequency of each character
    for char in word:
        freq[ord(char)] += 1
    
    # Count odd frequencies
    odd_count = 0
    total_half_length = 0
    
    for i in range(270):
        if freq[i] % 2 == 1:
            odd_count += 1
        freq[i] //= 2
        total_half_length += freq[i]
    
    # If more than one character has an odd frequency, no palindrome anagram is possible
    if odd_count > 1:
        return 0
    
    # Calculate the number of palindrome anagrams
    numerator = fact_mod_p_brute(total_half_length, MOD)
    denominator = 1
    
    for i in range(270):
        if freq[i] > 0:
            denominator *= fact_mod_p_brute(freq[i], MOD)
            denominator %= MOD
    
    # Use Fermat's Little Theorem to compute the modular inverse
    result = numerator * pow(denominator, MOD - 2, MOD) % MOD
    
    return result