"""
QUESTION:
Create a function `convert_list_to_dictionary` that takes a list of elements in the format [name, age, hobby] and converts it into a dictionary. Each dictionary entry should have a key-value pair where the key is the name of the person and the value is a dictionary containing their age and hobbies. The function should ensure the resulting dictionary does not contain duplicate entries for the same person, the age is converted to an integer, and the resulting dictionary is sorted alphabetically by the person's name. The hobbies should be stored as a list of strings. The solution should have a time complexity of O(n), where n is the number of elements in the list.
"""

def convert_list_to_dictionary(lst):
    dictionary = {}
    for i in range(0, len(lst), 3):
        name = lst[i]
        age = int(lst[i + 1])
        hobby = lst[i + 2]
        
        if name in dictionary:
            dictionary[name]['hobbies'].append(hobby)
        else:
            dictionary[name] = {'age': age, 'hobbies': [hobby]}
    
    for key in dictionary:
        dictionary[key]['hobbies'].sort()
    
    return dict(sorted(dictionary.items()))