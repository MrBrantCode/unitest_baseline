"""
QUESTION:
Create a function called `generate_month_list` that takes two parameters: a list to store the generated list of month names, and an integer to keep track of the current month being processed. Implement the function recursively without using any loops or iteration methods, and without any built-in functions or libraries to generate the list of month names. The function should return a list containing the full names of the 12 months in order, starting with January.
"""

def generate_month_list(months_list, current_month):
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    if current_month > 12:
        return months_list
    else:
        months_list.append(months[current_month - 1])
        return generate_month_list(months_list, current_month + 1)