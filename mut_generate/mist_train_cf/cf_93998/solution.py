"""
QUESTION:
Create a function `combine_lists_into_dict` that combines the elements of two lists of equal length into a dictionary. The dictionary should only include elements from list1 that have a corresponding element in list2 that is divisible by 2. If there is a repeating element in list1, it should be stored as a list of corresponding divisible elements in list2. The resulting dictionary should be sorted in descending order based on the values of the keys.
"""

def combine_lists_into_dict(list1, list2):
    result_dict = {}
    for i in range(len(list1)):
        if list2[i] % 2 == 0:
            if list1[i] in result_dict:
                result_dict[list1[i]].append(list2[i])
            else:
                result_dict[list1[i]] = [list2[i]]
    return dict(sorted(result_dict.items(), key=lambda x: x[0], reverse=True))