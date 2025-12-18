"""
QUESTION:
Write a function `parse_string(string)` that takes a string as input and returns a dictionary. The string contains words and numbers inside square brackets that indicate the repetition of the preceding word. If a number is not specified, the default repetition is 1. The function should store the words and their repetitions in the dictionary, where the words are the keys and the repetitions are the values. The dictionary should be sorted in descending order based on the repetitions, and if two words have the same repetition, they should be sorted alphabetically. The solution should have a time complexity of O(n), where n is the length of the input string, and a space complexity of O(m), where m is the number of unique words in the input string.
"""

def parse_string(string):
    word_dict = {}
    current_word = ""
    current_count = 1
    i = 0

    while i < len(string):
        if string[i] == "[":
            count = ""
            i += 1
            while i < len(string) and string[i].isdigit():
                count += string[i]
                i += 1
            if count == "":
                current_count = 1
            else:
                current_count = int(count)
            i += 1
        elif string[i].isalpha():
            current_word += string[i]
            i += 1
        else:
            if current_word != "":
                word_dict[current_word] = word_dict.get(current_word, 0) + current_count
                current_word = ""
                current_count = 1
            i += 1
    if current_word != "":
        word_dict[current_word] = word_dict.get(current_word, 0) + current_count
    
    sorted_dict = dict(sorted(word_dict.items(), key=lambda x: (-x[1], x[0])))
    return sorted_dict