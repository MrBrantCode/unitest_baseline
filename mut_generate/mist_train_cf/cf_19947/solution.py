"""
QUESTION:
Create a function called `find_anagrams` that takes a list of strings as input and returns a list of lists, where each inner list contains all anagrams of a particular string from the input list. The anagrams in each inner list should be sorted in alphabetical order, and there should be no duplicate anagrams across all inner lists. The time complexity of the function should be O(n*m*log(m) + k*log(k)), where n is the number of strings, m is the average length of the strings, and k is the number of unique anagrams. The space complexity should be O(n*m + k*m), where n is the number of strings, m is the average length of the strings, and k is the number of unique anagrams.
"""

def find_anagrams(strings):
    anagrams_dict = {}
    
    for string in strings:
        sorted_string = ''.join(sorted(string))
        if sorted_string in anagrams_dict:
            anagrams_dict[sorted_string].append(string)
        else:
            anagrams_dict[sorted_string] = [string]
    
    anagrams_list = [sorted(values) for values in anagrams_dict.values()]
    
    return sorted(anagrams_list, key=lambda x: (len(x), x[0]))