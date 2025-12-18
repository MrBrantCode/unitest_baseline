"""
QUESTION:
Create a function `create_vowel_dict` that takes a list of characters as input and returns a dictionary. 

The dictionary should have the index of each vowel in the list as the key and the sum of the ASCII values of its adjacent consonants as the value. 

The function should only include vowels that appear once in the list, are not at the beginning or end of the list, and are not adjacent to another vowel. The vowels should be identified by comparing them to the list ['a', 'e', 'i', 'o', 'u']. 

The function should ignore the case of the characters when comparing them to the list of vowels.
"""

def create_vowel_dict(char_list):
    """
    This function creates a dictionary where the keys are the indices of vowels in the input list
    and the values are the sum of ASCII values of adjacent consonants.

    Args:
        char_list (list): A list of characters.

    Returns:
        dict: A dictionary with vowel indices as keys and sum of ASCII values of adjacent consonants as values.
    """

    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_dict = {}
    char_list = [char.lower() for char in char_list]
    
    for index, char in enumerate(char_list):
        if (index != 0 and index != len(char_list) - 1 and 
            char in vowels and char_list.count(char) == 1 and 
            char_list[index-1] not in vowels and char_list[index+1] not in vowels):
            consonants_sum = ord(char_list[index-1]) + ord(char_list[index+1])
            vowel_dict[index] = consonants_sum

    return vowel_dict