"""
QUESTION:
Create a function `create_dictionary` that takes two lists, `name_list` and `age_list`, and returns a dictionary where the keys are names in lowercase and the values are their associated ages as strings. If there are duplicate names, append a number to the name in the dictionary to make it unique. The function should have a time complexity of O(n) and a space complexity of O(n), where n is the length of the `name_list`.
"""

def create_dictionary(name_list, age_list):
    name_dict = {}
    name_count = {}
    for i in range(len(name_list)):
        name = name_list[i].lower()
        age = str(age_list[i])
        
        if name in name_dict:
            name_count[name] += 1
            unique_name = name + "_" + str(name_count[name])
            name_dict[unique_name] = age
        else:
            name_dict[name] = age
            name_count[name] = 0
    
    return name_dict