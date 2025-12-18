"""
QUESTION:
Create a class with a constructor that takes a string as an argument. The class should have three methods: __len__ to return the length of the string, count_vowels to return the number of vowels ('a', 'e', 'i', 'o', 'u' in both uppercase and lowercase) in the string, and remove_duplicates to return a string with all duplicate characters removed while maintaining the original order. The count_vowels and remove_duplicates methods should not use any built-in string or list methods for counting vowels or removing duplicates, and instead use basic string manipulation techniques. The class should be implemented without using built-in Python functions or methods such as count(), lower(), or set() for the specified operations, except for the __len__ method which should return the length of the string.
"""

def entrance(string):
    def count_vowels():
        vowels = ['a', 'e', 'i', 'o', 'u']
        count = 0
        for char in string:
            if char.lower() in vowels:
                count += 1
        return count

    def remove_duplicates():
        result = ""
        seen = {}
        for char in string:
            if char not in seen:
                result += char
                seen[char] = True
        return result

    return len(string), count_vowels(), remove_duplicates()