"""
QUESTION:
Create a function called `find_anagrams` that takes a list of strings as input and returns a list of lists, where each sublist contains all possible anagrams for a given string in alphabetical order. The function should remove duplicate anagrams from the output list. The time complexity should be O(n*m*log(m) + k*log(k)) and the space complexity should be O(n*m + k*m), where n is the number of strings, m is the average length of the strings, and k is the number of unique anagrams.
"""

def find_anagrams(strings):
    anagrams_dict = {}
    
    for string in strings:
        sorted_string = ''.join(sorted(string))
        if sorted_string in anagrams_dict:
            anagrams_dict[sorted_string].append(string)
        else:
            anagrams_dict[sorted_string] = [string]
    
    anagrams_list = []
    for values in anagrams_dict.values():
        values.sort()
        anagrams_list.append(values)
    
    return sorted(anagrams_list, key=lambda x: (len(x), x[0]))