"""
QUESTION:
Compare two given strings and print the differences between them, ignoring differences in letter case, whitespace characters, punctuation marks, and special characters. The function should also indicate the positions of the differences and return the total number of differences found. The strings can be of any length.

The function name is not specified, but it should take two string parameters.
"""

def compare_strings(str1, str2):
    """
    Compare two given strings and print the differences between them, 
    ignoring differences in letter case, whitespace characters, punctuation marks, and special characters.

    Args:
        str1 (str): The first string.
        str2 (str): The second string.

    Returns:
        int: The total number of differences found.
    """

    # Convert strings to lower case and remove non-alphanumeric characters
    str1 = ''.join(e for e in str1 if e.isalnum() or e.isspace()).lower()
    str2 = ''.join(e for e in str2 if e.isalnum() or e.isspace()).lower()

    # Split the strings into words
    words1 = str1.split()
    words2 = str2.split()

    # Find the minimum length between the two lists of words
    min_length = min(len(words1), len(words2))

    # Initialize the count of differences
    diff_count = 0

    # Iterate over the words and compare them
    for i in range(min_length):
        if words1[i] != words2[i]:
            print(f"The word '{words1[i]}' is different in both strings. (Position: {i + 1})")
            diff_count += 1

    # If one string is longer than the other, count the extra words as differences
    diff_count += abs(len(words1) - len(words2))

    # Print the total number of differences
    print(f"Total differences found: {diff_count}")

    return diff_count