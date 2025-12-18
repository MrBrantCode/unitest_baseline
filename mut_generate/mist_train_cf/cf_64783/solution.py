"""
QUESTION:
Create a function `fruit_distribution(s, n, fruits, new_fruits_list)` that combines two lists of fruits (`fruits` and `new_fruits_list`) and returns a dictionary with the total count of each fruit type. The function should ignore the parameters `s` and `n`, and it should not modify the input lists. The dictionary should include all fruits from both lists, with their corresponding counts. If a fruit appears in both lists, its counts should be added. If a fruit only appears in one list, its count should be the number of times it appears in that list.
"""

def fruit_distribution(s, n, fruits, new_fruits_list):
    """
    Combines two lists of fruits and returns a dictionary with the total count of each fruit type.
    """
    fruit_dict = {}
    
    # Counting frequency of each fruit in the original fruits list
    for fruit in fruits:
        if fruit not in fruit_dict:
            fruit_dict[fruit] = 1
        else:
            fruit_dict[fruit] += 1

    # Counting frequency of each fruit in the new_fruits_list and adding it to the original fruit_dict
    for new_fruit in new_fruits_list:
        if new_fruit not in fruit_dict:
            fruit_dict[new_fruit] = 1
        else:
            fruit_dict[new_fruit] += 1

    return fruit_dict