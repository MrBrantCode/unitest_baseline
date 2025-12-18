"""
QUESTION:
Write a function `find_string_with_a` that iterates through a nested list of strings in reverse order. The function should print each string that contains the character 'a' (case-insensitive) a number of times equal to the string's 'a' count, and return the total count of such strings.
"""

def find_string_with_a(nested_list):
    count = 0
    for sublist in nested_list:
        for s in sublist[::-1]:
            appearances = s.lower().count('a')
            if appearances > 0:
                count += appearances
                print(s)
    return count