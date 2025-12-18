"""
QUESTION:
Write a recursive function `reverse_and_count_vowels` that takes a string as input and returns the count of unique vowels in the string. The function should also print the input string in reverse order. The count should not include duplicate vowels.
"""

def reverse_and_count_vowels(string, vowels=set(), count=0):
    # Base case: when string is empty, print reversed string and return the count
    if not string:
        print("Reversed string:", string[::-1])
        return count
    
    # Check if the first character is a vowel
    if string[0].lower() in "aeiou":
        # Exclude duplicate vowels from the count
        if string[0].lower() not in vowels:
            count += 1
            vowels.add(string[0].lower())
    
    # Recursively call the function with the remaining substring
    return reverse_and_count_vowels(string[1:], vowels, count)