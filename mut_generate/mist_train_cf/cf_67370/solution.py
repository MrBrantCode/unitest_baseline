"""
QUESTION:
Write a function `get_closest_vowel(word)` that finds the vowel in the input string `word` that is closest to the right side of the word and is located between two consonants. The function should distinguish between uppercase and lowercase vowels and ignore vowels at the beginning or end of the word. If such a vowel does not exist, return an empty string. Assume the input string only contains English letters.
"""

def get_closest_vowel(word):
    # check if word length is less than 3. Word must be at least 3 letters to have vowels between consonants
    if len(word) < 3: 
        return ''

    # convert word to whether each character is vowel or not
    # True for vowels, False for consonants
    is_vowel = ['aeiouAEIOU'.find(c) != -1 for c in word]

    # Iterate from right (excluding the last letter)
    for i in range(len(word)-2, 0, -1):
        # Check if this and surrounding letters are consonant-vowel-consonant
        if is_vowel[i-1] == is_vowel[i+1] == False and is_vowel[i] == True:
            return word[i]
    
    # Return empty string if no such vowel exists
    return ''