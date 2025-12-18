"""
QUESTION:
Create a function called `substring_indices` that accepts two string arguments, `str_1` and `str_2`. The function should return the starting and ending indices of all occurrences of `str_1` in `str_2`. If `str_1` does not appear in `str_2`, the function should return a meaningful message. The function should be case-sensitive.
"""

def substring_indices(str_1, str_2):
    freq = str_2.count(str_1)    #count the number of times str_1 occurs in str_2
    if freq == 0:    #if str_1 is not present in str_2
        return "The substring is not present within the main string"
    total_len = len(str_1)
    indices = []
    index = 0
    for i in range(freq):    #loop through the number of times str_1 occurs in str_2
        temp_index = str_2.find(str_1, index)    #find the first occurrence of str_1 in str_2 after index
        indices.append((temp_index, temp_index + total_len - 1))   #append the tuple of start and end indices to the list
        index = temp_index + 1    #update the index
    return indices