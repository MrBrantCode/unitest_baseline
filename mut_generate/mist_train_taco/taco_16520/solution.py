"""
QUESTION:
Create a program that reads the attendance numbers of students in a class and the data that stores the ABO blood group and outputs the number of people for each blood type. There are four types of ABO blood types: A, B, AB, and O.



Input

A comma-separated pair of attendance numbers and blood types is given over multiple lines. The attendance number is an integer between 1 and 50, and the blood type is one of the strings "A", "B", "AB" or "O". The number of students does not exceed 50.

Output

Number of people of type A on the first line
Number of people of type B on the second line
Number of people of AB type on the 3rd line
Number of O-shaped people on the 4th line
Is output.

Example

Input

1,B
2,A
3,B
4,AB
5,B
6,O
7,A
8,O
9,AB
10,A
11,A
12,B
13,AB
14,A


Output

5
4
3
2
"""

from collections import Counter

def count_blood_types(attendance_data):
    """
    Counts the number of people for each blood type from the given attendance data.

    Parameters:
    attendance_data (list of str): A list of strings where each string is a comma-separated pair of attendance number and blood type.

    Returns:
    dict: A dictionary with keys as blood types ("A", "B", "AB", "O") and values as their respective counts.
    """
    # Extract blood types from the attendance data
    blood_types = [entry.split(',')[1].strip() for entry in attendance_data]
    
    # Count the occurrences of each blood type
    blood_type_counts = Counter(blood_types)
    
    # Return the counts in a dictionary format
    return {
        'A': blood_type_counts.get('A', 0),
        'B': blood_type_counts.get('B', 0),
        'AB': blood_type_counts.get('AB', 0),
        'O': blood_type_counts.get('O', 0)
    }