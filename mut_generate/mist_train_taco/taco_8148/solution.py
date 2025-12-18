"""
QUESTION:
Given a string S of lowercase english characters. Rearrange characters of the given string such that the vowels and consonants occupy alternate positions and the string so formed should be lexicographically (alphabetically) smallest. 
Note: Vowels are 'a', 'e', 'i', 'o' and 'u'. 
Example 1:
Input:
S = "aeroplane"
Output: alanepero
Explanation: alanepero  
The vowels and consonants are arranged 
alternatively with vowels shown in bold.
Also, there's no lexicographically smaller
string possible with required conditions.
Example 2:
Input: 
S = "mississippi"
Output: -1
Explanation: The number of vowels is 4 
whereas the number of consonants is 7.
Hence, there's no way to arrange the
vowels and consonants alternatively.
Your Task:
You don't need to read input or print anything. Your task is to complete the function rearrange() which takes the string S and its size N as inputs and returns the modified string as stated in the description. If such a modification is not possible, return the string "-1".
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(2*26).
Constraints:
1 <= N <= 10^6
'a' <= S[ i ] <= 'z'
"""

def rearrange_string(S: str, N: int) -> str:
    if N == 1:
        return S
    
    vowels = {'a', 'e', 'i', 'o', 'u'}
    vowel_list = []
    consonant_list = []
    
    # Sort the string to get lexicographically smallest arrangement
    S = sorted(S)
    
    # Separate vowels and consonants
    for ch in S:
        if ch in vowels:
            vowel_list.append(ch)
        else:
            consonant_list.append(ch)
    
    # Check if rearrangement is possible
    if not (len(vowel_list) == len(consonant_list) or 
            len(vowel_list) == len(consonant_list) + 1 or 
            len(vowel_list) + 1 == len(consonant_list)):
        return "-1"
    
    # Determine which list is smaller and which is bigger
    if len(vowel_list) < len(consonant_list):
        small = vowel_list
        big = consonant_list
    elif len(vowel_list) > len(consonant_list):
        small = consonant_list
        big = vowel_list
    elif vowel_list[0] > consonant_list[0]:
        big = consonant_list
        small = vowel_list
    else:
        big = vowel_list
        small = consonant_list
    
    # Construct the new string with alternating characters
    new_s = ''
    for i in range(N):
        if i % 2 == 0:
            new_s += big[i // 2]
        else:
            new_s += small[i // 2]
    
    return new_s