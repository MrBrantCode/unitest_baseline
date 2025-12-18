"""
QUESTION:
Create a function called `bubble_sort` that sorts a list of numbers in ascending order using the Bubble Sort algorithm. The function should not create a new list, but instead modify the existing list.
"""

def bubble_sort(numerical_dataset):
    for pass_num in range(len(numerical_dataset) - 1, 0, -1):
        for i in range(pass_num):
            if numerical_dataset[i] > numerical_dataset[i+1]:
                temp = numerical_dataset[i]
                numerical_dataset[i] = numerical_dataset[i+1]
                numerical_dataset[i+1] = temp
    return numerical_dataset