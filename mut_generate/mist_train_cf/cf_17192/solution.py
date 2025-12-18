"""
QUESTION:
Write a function `convert_string_to_object_array` that takes a string `s` as input. Return an array of objects, where each object has two properties: "letter" and "count". The "letter" property stores a unique letter from the string, and the "count" property stores the number of times that letter appears in the string. The function must calculate the total count of all letters in the string, sort the array of objects in descending order based on the "count" property, and remove any objects with a "count" property less than or equal to 1. The implementation should only use basic array iteration and standard for loops.
"""

def convert_string_to_object_array(s):
    """
    Convert a string to an array of objects, where each object has two properties: 
    "letter" and "count". The "letter" property stores a unique letter from the string, 
    and the "count" property stores the number of times that letter appears in the string.
    
    Args:
        s (str): The input string.
    
    Returns:
        list: A list of objects with "letter" and "count" properties.
    """
    letter_count = {}
    total_count = 0

    for letter in s:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
        total_count += 1

    result = []
    for letter, count in letter_count.items():
        if count > 1:
            result.append({
                "letter": letter,
                "count": count
            })

    result.sort(key=lambda x: x["count"], reverse=True)
    return result