"""
QUESTION:
Create a function named `calculate_similarity_score` that compares two input strings and returns their similarity score. The score is based on common characters and their positions in the strings, ignoring case sensitivity. The function must apply a penalty of 0.2 to the score for each repeated character in either string and consider special characters, punctuation, and spaces during comparison. The function should handle strings of up to 10^6 characters efficiently.
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