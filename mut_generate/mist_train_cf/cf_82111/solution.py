"""
QUESTION:
Write a function called `count_vowels` that takes a list of strings as input, identifies the string with the maximum number of vowels, and returns the string along with the count of each vowel. The function should ignore non-string inputs and special characters, and it should consider both lowercase and uppercase vowels. The function should not take any other parameters besides the input list.
"""

def count_vowels(arr):
    """
    This function takes a list of strings, identifies the string with the maximum number of vowels, 
    and returns the string along with the count of each vowel.
    
    Parameters:
    arr (list): A list of strings.
    
    Returns:
    dict: A dictionary containing the string with the most vowels and the count of each vowel.
    """
    
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowels_count = {v: 0 for v in vowels}
    max_vowel_string = ""
    max_vowels = 0

    for element in arr:
        # Handle non-string inputs
        if not isinstance(element, str):
            continue 

        count = 0
        local_vowel_count = {v: 0 for v in vowels}
        for char in element.lower(): 
            if char in vowels: 
                count += 1
                local_vowel_count[char] += 1
        if count > max_vowels: 
            max_vowels = count
            max_vowel_string = element
            vowels_count = local_vowel_count

    result = {
        "string": max_vowel_string,
        "vowel_counts": vowels_count
    }
    return result