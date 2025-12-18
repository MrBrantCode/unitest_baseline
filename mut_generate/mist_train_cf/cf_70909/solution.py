"""
QUESTION:
Write a function called `palindrome_vowel_count` that takes a tuple of palindrome strings as a parameter and returns a dictionary where the palindromes are keys and the total count of vowels (both lowercase and uppercase) in each palindrome are the corresponding values.
"""

def palindrome_vowel_count(palindromes):
    vowels = "aeiouAEIOU"
    result = {}
    for word in palindromes:
        count = sum(1 for char in word if char in vowels)
        result[word] = count
    return result