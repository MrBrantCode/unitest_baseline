"""
QUESTION:
Write a function named "is_substring" that takes in two string parameters, "string1" and "string2". The function should return a boolean value indicating whether "string1" is a substring of "string2" or not, ignoring leading and trailing whitespaces, and performing a case-insensitive comparison. The function should not use any built-in functions or methods that directly solve this problem. It should have a time complexity of O(n), where n is the length of "string2".
"""

def is_substring(string1, string2):
    # Ignore leading and trailing whitespaces
    string1 = string1.strip()
    string2 = string2.strip()

    # Convert both strings to lowercase for case-insensitive comparison
    string1 = string1.lower()
    string2 = string2.lower()

    # Check if the length of string1 is greater than string2
    if len(string1) > len(string2):
        return False

    # Iterate over the characters of string2
    for i in range(len(string2)):
        # Check if the first character of string1 matches with the current character of string2
        if string1[0] == string2[i]:
            # Start a nested loop to compare the subsequent characters of string1 with string2
            for j in range(len(string1)):
                # Check if the characters match
                if string1[j] != string2[i+j]:
                    break
            else:
                # If all the characters of string1 match with string2, return True
                return True

    # If no match is found, return False
    return False