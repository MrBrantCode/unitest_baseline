"""
QUESTION:
Create a function called `main` that takes no arguments and performs the following operations: 
- Takes 10 unique integers within the range of -1000 to 1000 as input from the user.
- Stores the input integers in an array.
- Sorts the elements in the array in ascending order.
- Calculates and returns the median of the array.
"""

def validate_input(value, array):
    if value < -1000 or value > 1000:
        return False
    if value in array:
        return False
    return True

def get_input():
    valid_input = False
    while not valid_input:
        try:
            value = int(input("Enter a unique value between -1000 and 1000: "))
            return value
        except ValueError:
            print("Invalid input! Please enter an integer.")

def sort_array(array):
    array.sort()

def find_median(array):
    length = len(array)
    if length % 2 == 0:
        median = (array[length // 2 - 1] + array[length // 2]) / 2
    else:
        median = array[length // 2]
    return median

def main():
    array = []
    while len(array) < 10:
        value = get_input()
        if validate_input(value, array):
            array.append(value)
        else:
            print("Invalid input! Please enter a unique value between -1000 and 1000.")

    sort_array(array)
    median = find_median(array)
    return median