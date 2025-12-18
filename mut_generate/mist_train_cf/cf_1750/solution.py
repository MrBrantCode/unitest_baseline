"""
QUESTION:
Create a function called `find_common_characters` that takes two strings as input. It should return a dictionary where the keys are the common alphabetic characters between the two strings (considering uppercase and lowercase characters as the same) and the values are the number of occurrences of that character in both strings. The function should ignore any non-alphabetic characters in the input strings. The dictionary should be sorted by keys in alphabetical order. The function should have a time complexity of O(n+m) and a space complexity of O(min(n,m)), where n and m are the lengths of the input strings.
"""

def find_common_characters(str1, str2):
    # Ignore non-alphabetic characters and convert to lowercase
    str1 = ''.join(filter(str.isalpha, str1)).lower()
    str2 = ''.join(filter(str.isalpha, str2)).lower()
    
    # Count the occurrences of each character in both strings
    count1 = {}
    count2 = {}
    for char in str1:
        count1[char] = count1.get(char, 0) + 1
    for char in str2:
        count2[char] = count2.get(char, 0) + 1
    
    # Find the common characters and their occurrences
    common_chars = {}
    for char in count1:
        if char in count2:
            common_chars[char] = min(count1[char], count2[char])
    
    # Sort the common characters in alphabetical order
    common_chars = dict(sorted(common_chars.items()))
    
    return common_chars