"""
QUESTION:
Create a function `frequency_and_indexes` that takes a list containing integers and strings as input and returns a dictionary. The keys of the dictionary should be the elements from the list that occur at least five times, and the values should be tuples. The first element of the tuple should be the frequency of occurrence of the element, and the second element should be a list of index positions of each occurrence.
"""

from collections import defaultdict

def frequency_and_indexes(my_list):
  
    # Initialize a default dictionary. For every new key, it provides a default value.
    # Here the default value is a list [0,[]] which present frequency and the list of indexes respectively.
    count_dict = defaultdict(lambda: [0, []])
  
    for index, item in enumerate(my_list):
        count_dict[item][0] += 1  # increment frequency of occurrence
        count_dict[item][1].append(index)  # append the current index

    # Filter the dict and keep only those elements which occurs at least five times.
    count_dict = {key: value for key, value in count_dict.items() if value[0] >= 5}

    return count_dict