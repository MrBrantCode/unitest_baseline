"""
QUESTION:
Create a function `determine_age_group` that takes a Pandas DataFrame's "Age" column as input and returns a new column called "age_group" containing categorical values "young", "middle-aged", and "elderly" based on the following conditions:
- "young" for ages less than 25
- "middle-aged" for ages between 25 and 55 (inclusive)
- "elderly" for ages greater than 55
The solution should achieve a time complexity of O(n), where n is the number of rows in the DataFrame.
"""

def determine_age_group(age):
    if age < 25:
        return 'young'
    elif age >= 25 and age <= 55:
        return 'middle-aged'
    else:
        return 'elderly'