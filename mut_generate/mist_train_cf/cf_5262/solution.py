"""
QUESTION:
Create a function named `get_anagrams` that takes a list of strings as input and returns a list of lists, where each sublist contains all possible anagrams for a string in the input list. The anagrams should be sorted in alphabetical order, and duplicates should be removed from the output list. The function should handle strings with non-alphabetic characters and whitespace. The function should have a time complexity of O(n*m*log(m) + k*log(k)) and a space complexity of O(n*m + k*m), where n is the number of strings in the input list, m is the average length of the strings, and k is the number of unique anagrams.
"""

def get_anagrams(string_list):
    def get_sorted_string(string):
        # Remove non-alphabetic characters and convert to lowercase
        string = ''.join(ch.lower() for ch in string if ch.isalpha())
        # Sort the characters of the string
        return ''.join(sorted(string))

    anagram_dict = {}
    
    for string in string_list:
        sorted_string = get_sorted_string(string)
        if sorted_string in anagram_dict:
            anagram_dict[sorted_string].append(string)
        else:
            anagram_dict[sorted_string] = [string]
    
    return [sorted(anagram_list) for anagram_list in anagram_dict.values() if len(anagram_list) > 1]