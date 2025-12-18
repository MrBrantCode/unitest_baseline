"""
QUESTION:
Write a function `is_substring(main_string, target_string)` that takes in two strings and returns a boolean indicating whether the target string is a substring of the main string, ignoring case differences. The function should not use any built-in string manipulation functions or methods, external libraries, or allocate extra memory. It should have a time complexity of O(n + m), where n and m are the lengths of the main string and the target string, respectively, and a space complexity of O(1).
"""

def is_substring(main_string, target_string):
    main_length = len(main_string)
    target_length = len(target_string)

    for i in range(main_length - target_length + 1):
        j = 0
        while j < target_length:
            if main_string[i+j].lower() != target_string[j].lower():
                break
            j += 1

        if j == target_length:
            return True

    return False