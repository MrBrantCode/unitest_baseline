"""
QUESTION:
Given a string S, sort it in the following manner. Sorted string must contain a vowel as first letter and a consonant as next letter and so on OR a consonant as first letter and a vowel as next letter and so on, depending on the string. If there is no vowel left then print the remaining consonant in ascending order and vice versa. 
Note: Order of vowel must be a->e->i->o->u and order of consonant must be b->c->d... and so on.
Example 1: 
Input: abcdei 
Output: abecid 
Explanation: 'a' (Vowel) came first so the
pattern of sorted string is vcvcvcvc... 
Example 2: 
Input: bcadefgh
Output: bacedfgh 
Explanation: 'b' (consonant) came first so
the pattern of sorted string is cvcvcvcv....
 
Your Task: 
You don't need to read input or print anything. Your task is to complete the function SortedString() which takes the string s as input parameters and returns the sorted string. 
 
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
 
Constraints:
1<=|S|<=1000000
"""

def sorted_string(s: str) -> str:
    vowels_set = 'aeiou'
    vowels = []
    consonants = []
    
    # Separate vowels and consonants
    for char in s:
        if char in vowels_set:
            vowels.append(char)
        else:
            consonants.append(char)
    
    # Sort vowels and consonants
    vowels.sort()
    consonants.sort()
    
    result = []
    if s[0] in vowels_set:
        # Start with vowels
        for v, c in zip(vowels, consonants):
            result.append(v)
            result.append(c)
        # Append remaining characters
        result.extend(vowels[len(consonants):])
        result.extend(consonants[len(vowels):])
    else:
        # Start with consonants
        for c, v in zip(consonants, vowels):
            result.append(c)
            result.append(v)
        # Append remaining characters
        result.extend(consonants[len(vowels):])
        result.extend(vowels[len(consonants):])
    
    return ''.join(result)