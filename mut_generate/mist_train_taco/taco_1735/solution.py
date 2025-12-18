"""
QUESTION:
Vasya decided to write an anonymous letter cutting the letters out of a newspaper heading. He knows heading s1 and text s2 that he wants to send. Vasya can use every single heading letter no more than once. Vasya doesn't have to cut the spaces out of the heading — he just leaves some blank space to mark them. Help him; find out if he will manage to compose the needed text.

Input

The first line contains a newspaper heading s1. The second line contains the letter text s2. s1 и s2 are non-empty lines consisting of spaces, uppercase and lowercase Latin letters, whose lengths do not exceed 200 symbols. The uppercase and lowercase letters should be differentiated. Vasya does not cut spaces out of the heading.

Output

If Vasya can write the given anonymous letter, print YES, otherwise print NO

Examples

Input

Instead of dogging Your footsteps it disappears but you dont notice anything
where is your dog


Output

NO


Input

Instead of dogging Your footsteps it disappears but you dont notice anything
Your dog is upstears


Output

YES


Input

Instead of dogging your footsteps it disappears but you dont notice anything
Your dog is upstears


Output

NO


Input

abcdefg hijk
k j i h g f e d c b a


Output

YES
"""

def can_compose_letter(s1: str, s2: str) -> str:
    # Remove spaces from both strings
    s1 = ''.join(s1.split())
    s2 = ''.join(s2.split())
    
    # Create a dictionary to count occurrences of each character in s1
    s1_count = {}
    for char in s1:
        if char in s1_count:
            s1_count[char] += 1
        else:
            s1_count[char] = 1
    
    # Check if s2 can be composed using characters from s1
    for char in s2:
        if char not in s1_count or s1_count[char] == 0:
            return "NO"
        s1_count[char] -= 1
    
    return "YES"