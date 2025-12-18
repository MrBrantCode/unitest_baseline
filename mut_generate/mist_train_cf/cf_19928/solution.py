"""
QUESTION:
Design a recursive function `reverse_string_vowels_consonants` that takes a string of lowercase alphabets as input and prints the string in reverse order, counts the number of unique vowels, and returns the number of consonants. The input string is guaranteed to contain at least one vowel and no special characters or spaces.
"""

def reverse_string_vowels_consonants(string):
    """
    This function takes a string of lowercase alphabets, prints the string in reverse order, 
    counts the number of unique vowels, and returns the number of consonants.
    
    Parameters:
    string (str): A string of lowercase alphabets.
    
    Returns:
    int: The number of consonants in the string.
    """
    
    vowels = set(['a', 'e', 'i', 'o', 'u'])
    consonants = set()
    count_vowels = 0
    count_consonants = 0
    
    def helper(string):
        nonlocal count_vowels
        nonlocal count_consonants
        
        if string == "":
            return ""
        
        if string[0] in vowels:
            if string[0] not in consonants:
                count_vowels += 1
        else:
            count_consonants += 1
            consonants.add(string[0])
        
        return helper(string[1:]) + string[0]
    
    reversed_string = helper(string)
    
    print("Reversed String:", reversed_string)
    print("Vowels:", len(set([char for char in string if char in vowels])))
    print("Consonants:", count_consonants)
    
    return count_consonants