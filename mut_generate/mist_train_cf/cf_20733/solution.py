"""
QUESTION:
Create a function `calculate_similarity_score(string1, string2)` to compare two strings and output their similarity score. The score is calculated based on the number of common characters between the strings, considering both the character and its position in the strings. The comparison is case-insensitive, and the function should ignore case sensitivity by treating "Python" and "pYTHON" as identical strings.

The function should implement a penalty system, subtracting 0.2 from the similarity score for every repeated character in each string. It should consider special characters, punctuation, and spaces when comparing the strings. The function should handle strings with a length of up to 10^6 characters efficiently, aiming for a time complexity of O(n) or better.
"""

def calculate_similarity_score(string1, string2):
    # Convert both strings to lowercase to ignore case sensitivity
    string1 = string1.lower()
    string2 = string2.lower()

    # Create a dictionary to store the count of characters in each string
    char_count1 = {}
    char_count2 = {}

    # Initialize similarity score
    similarity_score = 0

    # Iterate over the characters in string1
    for char in string1:
        # Ignore special characters, punctuation, and spaces
        if char.isalpha():
            # If the character is already in char_count1, decrease the similarity score
            if char in char_count1:
                similarity_score -= 0.2
            else:
                char_count1[char] = 1

    # Iterate over the characters in string2
    for char in string2:
        # Ignore special characters, punctuation, and spaces
        if char.isalpha():
            # If the character is already in char_count2, decrease the similarity score
            if char in char_count2:
                similarity_score -= 0.2
            else:
                char_count2[char] = 1

            # If the character is also present in string1, increase the similarity score
            if char in char_count1:
                similarity_score += 1
                # Remove the character from char_count1 to handle multiple occurrences of the same character in string1
                del char_count1[char]

    return similarity_score