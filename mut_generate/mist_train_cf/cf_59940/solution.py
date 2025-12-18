"""
QUESTION:
Create a function named `trimmed_mean` that takes in a list `l` containing numeric values (including negative integers and complex numbers) and a `trim_percentage` float value. The function should calculate the trimmed mean of the elements in the list by first sorting them based on their real values, then removing the specified percentage of elements from both ends of the sorted list, and finally returning the mean of the remaining elements. The function should not use any pre-established library functions and should handle empty lists or lists where the number of elements to trim exceeds the total number of elements.
"""

def trimmed_mean(l: list, trim_percentage: float):
    if not l: 
        return 0.0

    total_elements = len(l)
    trim_elements = int(total_elements * trim_percentage)

    sorted_l = sorted(l, key=lambda x:x.real)

    if trim_elements > total_elements:
        return 0.0 

    sorted_l = sorted_l[trim_elements: total_elements-trim_elements] 
    
    mean_val = sum(sorted_l)/len(sorted_l)

    return mean_val.real