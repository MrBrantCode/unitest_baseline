"""
QUESTION:
Write a function named `is_substring` that takes two strings, `main_string` and `target_string`, and returns a boolean indicating whether `target_string` is a substring of `main_string`. The function should be case-insensitive, handle both uppercase and lowercase characters, and should not use any built-in string manipulation functions or methods, or external libraries. The time complexity of the solution should be O(n * m), where n is the length of `main_string` and m is the length of `target_string`, and the space complexity should be O(1).
"""

def is_substring(main_string, target_string):
    main_len = len(main_string)
    target_len = len(target_string)

    if target_len > main_len:
        return False

    for i in range(main_len - target_len + 1):
        match = True
        for j in range(target_len):
            if main_string[i+j].lower() != target_string[j].lower():
                match = False
                break
        if match:
            return True

    return False