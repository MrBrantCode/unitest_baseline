"""
QUESTION:
Write a recursive function `find_max_consecutive_vowels` that takes a string `s` and returns the maximum number of consecutive vowels in the string and all substrings containing the maximum number of consecutive vowels. The function should handle both uppercase and lowercase vowels, special characters, and numbers. It should also handle cases where there are multiple substrings with the same maximum number of consecutive vowels. The input string will not be empty and the function should only iterate through the string once without using built-in string manipulation functions, regular expressions, or additional data structures.
"""

def find_max_consecutive_vowels(s, max_count=0, max_substrings=[], count=0, substring=""):
    if s == "":
        if count > max_count:
            max_count = count
            max_substrings = [substring]
        elif count == max_count and count > 0:
            max_substrings.append(substring)
        return max_count, max_substrings
    
    if s[0].lower() in "aeiou":
        count += 1
        substring += s[0]
    else:
        if count > max_count:
            max_count = count
            max_substrings = [substring]
        elif count == max_count and count > 0:
            max_substrings.append(substring)
        count = 0
        substring = ""
    
    return find_max_consecutive_vowels(s[1:], max_count, max_substrings, count, substring)