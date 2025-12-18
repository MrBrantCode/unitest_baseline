"""
QUESTION:
Write a function `find_vowels(text)` that prints the position and letter of each vowel in the given text and returns the total number of vowels. The function should handle both uppercase and lowercase vowels, special characters, and spaces, considering them as non-vowels. The time complexity should be O(n), where n is the length of the text, and the space complexity should be O(1), excluding the space used for the output.
"""

def find_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_count = 0

    for i in range(len(text)):
        char = text[i].lower()
        if char in vowels:
            vowel_count += 1
            print(f"Vowel found at position {i+1}: {char}")

    print(f"Total number of vowels: {vowel_count}")
    return vowel_count