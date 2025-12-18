"""
QUESTION:
Write a function `longest_palindromic_subsegment(textual_fragment)` that finds the longest subsegments in a given string `textual_fragment` that form a palindrome and consist of twin characters (i.e., characters that appear side by side like "oo" or "aa"). If there are multiple subsegments with the same longest length, return all of them. If there are no palindromic subsegments, return "There is no palindromic subsegments."
"""

def longest_palindromic_subsegment(textual_fragment):
    length = len(textual_fragment)
    result = []

    max_length = 0
    for i in range(length):
        temp_string = textual_fragment[i]
        for j in range(i + 1, length):
            if textual_fragment[i] == textual_fragment[j]:
                temp_string += textual_fragment[j]
            else:
                break
        if temp_string == temp_string[::-1] and len(temp_string) > max_length:
            max_length = len(temp_string)
            result = [temp_string]
        elif temp_string == temp_string[::-1] and len(temp_string) == max_length:
            result.append(temp_string)
    
    if len(result) == 0:
        return "There is no palindromic subsegments."
    
    return result