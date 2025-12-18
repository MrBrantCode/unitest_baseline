"""
QUESTION:
Create a function `get_anagrams` that takes a list of strings and returns a list of all possible anagrams for each string, with the anagrams sorted in alphabetical order. The function should remove duplicate anagrams from the output list. The function should also handle strings with non-alphabetic characters and whitespace. The time complexity should be O(n*m*log(m) + k*log(k)), where n is the number of strings in the input list, m is the average length of the strings, and k is the number of unique anagrams. The space complexity should be O(n*m + k*m), where n is the number of strings in the input list, m is the average length of the strings, and k is the number of unique anagrams.
"""

def get_anagrams(string_list):
    def get_sorted_string(string):
        return ''.join(sorted(''.join(ch.lower() for ch in string if ch.isalpha())))

    anagram_dict = {}
    
    for string in string_list:
        sorted_string = get_sorted_string(string)
        if sorted_string in anagram_dict:
            anagram_dict[sorted_string].append(string)
        else:
            anagram_dict[sorted_string] = [string]
    
    return list(anagram_dict.values())