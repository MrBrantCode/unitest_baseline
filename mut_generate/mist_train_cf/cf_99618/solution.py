"""
QUESTION:
Write a function `find_least_common_values` that takes a list of integers as input, filters out values outside the range [7, 12], counts the frequency of each remaining value, and returns a list of lists where the first column contains the three least common values in ascending order and the second column contains their corresponding frequencies in descending order. The function should be reusable for similar analyses.
"""

def find_least_common_values(lst):
    # Filter the list to only include values between 7 and 12
    filtered_lst = [x for x in lst if x >= 7 and x <= 12]
    
    # Count the frequency of each value in the filtered list
    freq_dict = {}
    for x in filtered_lst:
        if x in freq_dict:
            freq_dict[x] += 1
        else:
            freq_dict[x] = 1
    
    # Sort the values in ascending order by frequency
    sorted_freq = sorted(freq_dict.items(), key=lambda x: x[1])
    
    # Extract the three least common values (if possible)
    least_common_values = []
    for i in range(min(3, len(sorted_freq))):
        least_common_values.append(sorted_freq[i][0])
    
    # Create a table with the values and their frequencies
    table = []
    for x in least_common_values:
        freq = freq_dict[x]
        table.append([x, freq])
    
    # Sort the table based on values in ascending order and frequencies in descending order
    table.sort(key=lambda x: (x[0], -x[1]))
    
    return table