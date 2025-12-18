"""
QUESTION:
Create a function `remove_duplicates` that takes a list of integers as input. The function should return a dictionary where keys are the unique integers from the list and values are their occurrence counts. The function should also handle potential errors or exceptions.
"""

def remove_duplicates(input_list):
    number_counts = {}
    try:
        for number in input_list:
            if number in number_counts:
                number_counts[number] += 1
            else:
                number_counts[number] = 1
        return number_counts
    except Exception as e:
        print(f"An error occurred: {e}")