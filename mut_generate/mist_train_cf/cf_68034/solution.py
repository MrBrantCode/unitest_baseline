"""
QUESTION:
Develop a function called `find_max_secmax_avg` that takes a list of mixed data types as input, filters out non-numeric values, and returns a tuple containing the maximum value, the second maximum value, and the average of the numeric values. If the input list is empty or contains no numeric values, return `(None, None, None)`. If the input list contains only one numeric value, return a tuple with the value, `None`, and the value as the average.
"""

def find_max_secmax_avg(data):
    # Take care of the case if the dataset is empty
    if len(data) == 0: 
        return None, None, None

    # Filter out the non-numeric values
    num_list = [i for i in data if isinstance(i, (int, float))]

    # If there are no numeric values in the dataset
    if len(num_list) <= 0:
        return None, None, None

    max_num = max(num_list)
    num_list.remove(max_num)
    
    #If there is only one number in the dataset, return the max_num, None for 2nd largest, and the max_num for the average
    if len(num_list) == 0: 
        return max_num, None, max_num 

    secmax_num = max(num_list)
    avg_num = sum(num_list+[max_num]) / len(num_list+[max_num])

    return max_num, secmax_num, avg_num