"""
QUESTION:
Write a function named `classify_elements` that categorizes the elements of a provided list into three clusters: small (less than 10), medium (between 10 and 20), and large (greater than 20), excluding out of range values (less than 0 or greater than 100) and handling duplicate elements by only including unique values in each cluster.
"""

def classify_elements(lst):
    small = []  # for elements less than 10
    medium = []  # for elements between 10 and 20
    large = []  # for elements more than 20

    for num in lst:
        if num < 0 or num > 100:  # skip out of range values
            continue
        elif num < 10:  # if the number is less than 10
            if num not in small:  # check for duplicates
                small.append(num)
        elif 10 <= num <= 20:  # if the number is between 10 and 20
            if num not in medium:  # check for duplicates
                medium.append(num)
        else:  # for number greater than 20
            if num not in large:  # check for duplicates
                large.append(num)

    return {'small': small, 'medium': medium, 'large': large}