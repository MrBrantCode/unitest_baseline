"""
QUESTION:
Write a function named `detect_anagrams` that takes a list of strings as input and returns a dictionary where the keys are the input strings and the values are lists of anagrams for each string. The function should have a time complexity of O(n*m^2), where n is the number of strings in the input list and m is the average length of the strings.
"""

def detect_anagrams(strings):
    anagram_dict = {}
    
    # Iterate over each string in the input list
    for string in strings:
        # Create a sorted string as the key for the anagram dictionary
        sorted_string = ''.join(sorted(string))
        
        # Check if the sorted string already exists as a key in the dictionary
        if sorted_string in anagram_dict:
            # If it exists, append the current string to the list of anagrams
            anagram_dict[sorted_string].append(string)
        else:
            # If it doesn't exist, create a new key-value pair with the sorted string as the key and the current string as the first value in the list
            anagram_dict[sorted_string] = [string]
    
    # Remove the keys with an empty list value, since they don't have any anagrams
    anagram_dict = {key: value for key, value in anagram_dict.items() if len(value) > 1}
    
    return anagram_dict