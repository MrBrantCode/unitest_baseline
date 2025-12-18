"""
QUESTION:
Create a function `reverseVowels(s)` that inverts the positions of all the vowels present in the string `s`, while leaving the other characters in their original places. The vowels to be considered are 'a', 'e', 'i', 'o', 'u' in both lowercase and uppercase. The function should work with strings of length within the range of 1 <= s.length <= 3 * 10^5 that only contain printable ASCII characters.
"""

def reverseVowels(s: str) -> str:
    vowels = set('aeiouAEIOU')  
    s = list(s)  
    left, right = 0, len(s) - 1  

    while left < right:  
        if s[left] not in vowels:  
            left += 1  
        elif s[right] not in vowels:  
            right -= 1  
        else:  
            s[left], s[right] = s[right], s[left]  
            left, right = left + 1, right - 1  

    return ''.join(s)  