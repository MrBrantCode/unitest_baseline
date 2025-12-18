"""
QUESTION:
Write a function named `is_substring` that takes two strings, `main_string` and `target_string`, as input and returns a boolean value. The function should determine whether the `target_string` is a substring of the `main_string` in a case-insensitive manner. The function should have a time complexity of O(n + m), where n is the length of `main_string` and m is the length of `target_string`, and a space complexity of O(1), meaning no additional data structures or memory allocation should be used.
"""

def entrance(main_string, target_string):
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