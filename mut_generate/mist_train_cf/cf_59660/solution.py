"""
QUESTION:
Create a function named `string_analysis` that takes a string as input and returns a dictionary where each key is a character from the string and its corresponding value is a tuple. The tuple should contain the number of occurrences of the character in the string and a list of its index positions. If the character is a vowel ('a', 'e', 'i', 'o', 'u'), the tuple should also include the binary representation of the character as its third element.
"""

def string_analysis(string):
    vowels = 'aeiou'
    analysis_dict = {}
    for index, char in enumerate(string):
        if char in analysis_dict:
            count, positions, *binary = analysis_dict[char]
            analysis_dict[char] = (count+1, positions + [index], *binary)
        else:
            if char in vowels:
                analysis_dict[char] = (1, [index], format(ord(char), 'b'))
            else:
                analysis_dict[char] = (1, [index])
    return analysis_dict